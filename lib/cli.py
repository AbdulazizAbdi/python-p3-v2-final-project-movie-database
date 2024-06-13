# lib/cli.py

from helpers import (
    exit_program,
    list_genres,
    find_genre_by_name,
    find_genre_by_id,
    create_genre,
    update_genre,
    delete_genre,
    list_movies,
    find_movie_by_title,
    find_movie_by_id,
    create_movie,
    update_movie,
    delete_movie,
    list_of_genres_movies
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_genres()
        elif choice == "2":
            find_genre_by_id()
        elif choice == "3":
            find_genre_by_name()
        elif choice == "4":
            create_genre()
        elif choice == "5":
            update_genre()
        elif choice == "6":
            delete_genre()
        elif choice == "7":
            list_movies()
        elif choice == "8":
            find_movie_by_id()
        elif choice == "9":
            find_movie_by_title()
        elif choice == "10":
            create_movie()
        elif choice == "11":
            update_movie()
        elif choice == "12":
            delete_movie()
        elif choice == "13":
            list_of_genres_movies()
        else:
            print("Invalid choice")


def menu():
    print("MOVIE DATABASE MANAGER")
    print("Genre Options")
    print("Please select an Genre option from 1 - 6:")
    print("0. Exit the program")
    print("1. Genre List")
    print("2. Find Genre by id")
    print("3. Find Genre by name")
    print("4: Create new genre")
    print("5: Update existing genre")
    print("6: Delete genres")
    print("Movie Options")
    print("Please select an Movie option from 7 - 13:")
    print("7. Movie List")
    print("8. Find Movie by id")
    print("9. Find Movie by title")
    print("10: Create new movie")
    print("11: Update existing movie")
    print("12: Delete movie")
    print("13: List all movies in a genre")


if __name__ == "__main__":
    main()
