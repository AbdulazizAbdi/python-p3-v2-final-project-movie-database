# Phase 3 CLI+ORM Project: Movie Database Manager

---

## Introduction

This repository contains a CLI+ORM application that allows for movies to be stored in a database according to their genres.

Fork and clone this repisotory to your local device and set up the environment first in the next section below.

This is the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── genre.py
    │   └── movie.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```
---

## Generating Your Environment

After forking an d cloning this repository on to your local device then run the commands below to install the dependencies from the Pipfile:

```console
pipenv install
pipenv shell
```

## Generating The CLI Application

After generating the environment and entering the shell environment, Follow the steps below to use the CLI application:

1. Seed the database to load and initialize the database to allow for use of the CLI features with step 2.
2. Populate the database using `python lib/debug.py`, After receiving the message "Database Populated" move to the next step.
3. You can now run the code using `python lib/cli.py` and test the code and functionalities on the CLI application.

## Description

The CLI application has two modal classes in the `lib/models` directory, Movie and Genre. 
The classes have a one to many relationship where one genre has many movies and a movie 
can only have one genre. 

The `helpers.py` file contains the methods that give functionality to the CLI input 
prompts you generated in the above section. The CLI has a menu with functionalities 
for both tables in the database, **movies and genres**.