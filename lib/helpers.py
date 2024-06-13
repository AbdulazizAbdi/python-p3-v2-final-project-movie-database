# lib/helpers.py

from models.genre import Genre
from models.movie import Movie


def exit_program():
    print("Goodbye!")
    exit()

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(genre)


def find_genre_by_name():
    name = input("Please enter the genre's name: ")
    genre = Genre.find_by_name(name)
    print(genre) if genre else print(
        f'This Genre: {name} is not available')


def find_genre_by_id():
    id_ = input("Please enter the genre's id: ")
    genre = Genre.find_by_id(id_)
    print(genre) if genre else print(f'This Genre: {id_} is not available')


def create_genre():
    name = input("Please enter the genre's name: ")
    description = input("Please enter the genre's description: ")
    try:
        genre = Genre.create(name, description)
        print(f'Genre created: {genre}')
    except Exception as exc:
        print("Unable to create new genre: ", exc)


def update_genre():
    id_ = input("Please enter the genre's id: ")
    if genre := Genre.find_by_id(id_):
        try:
            name = input("Please enter the genre's updated name: ")
            genre.name = name
            description = input("Please enter the genre's updated description: ")
            genre.description = description

            genre.update()
            print(f'Genre updated: {genre}')
        except Exception as exc:
            print("Unable to update genre: ", exc)
    else:
        print(f'This Genre: {id_} is not available')


def delete_genre():
    id_ = input("Please enter the genre's id: ")
    if genre := Genre.find_by_id(id_):
        genre.delete()
        print(f'This Genre: {id_} has been deleted')
    else:
        print(f'This Genre: {id_} is not available')

def list_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(movie)


def find_movie_by_title():
    title = input("Please enter the movie's title: ")
    movie = Movie.find_by_title(title)
    print(movie) if movie else print(
        f'This Movie: {name} is not available')


def find_movie_by_id():
    id_ = input("Please enter the movie's id: ")
    movie = Movie.find_by_id(id_)
    print(movie) if movie else print(f'This Movie: {id_} is not available')


def create_movie():
    title = input("Please enter the new movie's title: ")
    runtime = input("Please enter the new movie's runtime: ")
    age_rating = input("Please enter the new movie's age rating: ")
    genre_id = input("Please enter the new movie's genre id: ")
    try:
        runtime = int(runtime)
        age_rating = int(age_rating)
        genre_id = int(genre_id)

        movie = Movie.create(title, runtime, age_rating, genre_id)
        print(f'Movie created: {movie}')
    except Exception as exc:
        print("Unable to create new movie: ", exc)


def update_movie():
    id_ = input("Please enter the movie's id: ")
    if movie := Movie.find_by_id(id_):
        try:
            title = input("Please enter the new movie's title: ")
            movie.title = title

            runtime = input("Please enter the new movie's runtime: ")
            runtime = int(runtime)
            movie.runtime = runtime

            age_rating = input("Please enter the new movie's age rating: ")
            age_rating = int(age_rating)
            movie.age_rating = age_rating

            genre_id = input("Please enter the new movie's genre id: ")
            genre_id = int(genre_id)
            movie.genre_id = genre_id

            movie.update()
            print(f'Movie Updated: {movie}')
        except Exception as exc:
            print("Unable to update movie: ", exc)
    else:
        print(f'This Movie: {id_} is not available')


def delete_movie():
    id_ = input("Please enter the movie's id: ")
    if movie := Movie.find_by_id(id_):
        movie.delete()
        print(f'This Movie: {id_} has been deleted')
    else:
        print(f'This Movie: {id_} is not available')

def list_of_genres_movies():
    id_ = input("Please enter the genre's id: ")
    id_ = int(id_)
    if genre := Genre.find_by_id(id_):
        try:
            movies_list = []
            movies = Movie.get_all()
            for movie in movies:
                if movie.genre_id == id_:
                    movies_list.append(movie)

            print(movies_list)
        except:
            print("No movies's are in this genre")
        
    else:
        print(f'This Genre: {id_} is not available')
