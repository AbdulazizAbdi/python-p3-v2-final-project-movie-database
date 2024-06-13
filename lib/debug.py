#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.movie import Movie
#import ipdb

def seed_database():
    Movie.drop_table()
    Genre.drop_table()
    Genre.create_table()
    Movie.create_table()

    # Create seed data
    action = Genre.create("Action", "High octane nonstop entertainment")
    comedy = Genre.create("Comedy", "Funny, Always laughing")

    Movie.create("Avengers", 118, 13, action.id)
    Movie.create("XMen", 132, 16, action.id)
    Movie.create("Spiderman", 202, 10, action.id)
    Movie.create("Simpsons The Movie", 90, 18, comedy.id)
    Movie.create("Die Hard", 155, 19, comedy.id)


seed_database()
print("Seeded database")

#ipdb.set_trace()
