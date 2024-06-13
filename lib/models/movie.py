from models.__init__ import CURSOR, CONN
from models.genre import Genre

class Movie:

    all = {}

    def __init__(self, title, runtime, age_rating, genre_id, id = None):
        self.id = id
        self.title = title
        self.runtime = runtime
        self.age_rating = age_rating
        self.genre_id = genre_id

    def __repr__(self):
        return (
            f"<Movie {self.id}: {self.title}, Runtime: {self.runtime} mins, PG: {self.age_rating} " +
            f"Genre ID: {self.genre_id}>"
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def runtime(self):
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        if isinstance(runtime, int) and runtime > 0:
            self._runtime = runtime
        else:
            raise ValueError("Runtime must be an integer greater than 0")

    @property
    def age_rating(self):
        return self._age_rating

    @age_rating.setter
    def age_rating(self, age_rating):
        if isinstance(age_rating, int) and age_rating > 0:
            self._age_rating = age_rating
        else:
            raise ValueError("Age Rating must be an integer greater than 0")

    @property
    def genre_id(self):
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        if type(genre_id) is int and Genre.find_by_id(genre_id):
            self._genre_id =genre_id
        else:
            raise ValueError("genre_id must be a genre stored in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            runtime INTEGER,
            age_rating INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movies;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO movies (title, runtime, age_rating, genre_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.runtime, self.age_rating, self.genre_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, runtime, age_rating, genre_id):
        movie = cls(title, runtime, age_rating, genre_id)
        movie.save()
        return movie

    def update(self):
        sql = """
            UPDATE movies
            SET title = ?, runtime = ?, age_rating = ?, genre_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.runtime, self.age_rating, self.genre_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM movies
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        movie = cls.all.get(row[0])
        if movie:
            movie.title = row[1]
            movie.runtime = row[2]
            movie.age_rating = row[3]
            movie.genre_id= row[4]
        else:
            movie = cls(row[1], row[2], row[3], row[4])
            movie.id = row[0]
            cls.all[movie.id] = movie
        return movie

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movies
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM movies
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM movies
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None