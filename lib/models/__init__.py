import sqlite3

CONN = sqlite3.connect('movie.db')
CURSOR = CONN.cursor()
