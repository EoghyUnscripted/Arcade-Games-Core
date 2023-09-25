# Arcade Games

## Overview

Every Christmas growing up, I was always wishing for a new game or console and I would usually get it because my mother would get the poor family bundle like everyone else I knew. They would always come with a starter arcade game that had a load of generic games on it which we all played at least once.

I built this core Python program for the nostalgia. And those of you that remember the green screen, you'll enjoy this little trip down memory lane, too.

## Setup

1. Install the [Requests]("https://pypi.org/project/requests/") library if you do not already have it installed on your environment

    In new terminal/console window:

    ```python
    pip install requests
    ```

## Games

1. Blackjack
2. Hangman
3. Quiz Game

## File Hierarchy Glossary

### Apps Folder

This directory hosts all of the required application file packages for the parent program or directory. Usually includes self-contained packages with it's own subdirectories like `Blackboard` or `Hangman`.

### Classes Folder

This directory hosts all of the python Class files required for use with the parent program or directory. For example, the `Brain.py` and `Question.py` class files will reside here for the "Quiz Game" subdirectory.

### Data Folder

This directory hosts all of the required data for the parent program or directory. This includes any app-related data such as SQLite databases, JSON files, APIs, etc.

### Modules Folder

This directory contains all of the required module files to operate the primary application `server.py`. This directory includes all globally used functions, methods, and data like the menu.
