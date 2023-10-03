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

## Run

This is a core application and can be called in the command line interface (CLI) directly or run using an IDE like Visual Studio Code. Simply call the `server.py` file and it will run automatically.

## Games

1. Blackjack
2. Hangman
3. Rock, Paper, Scissors
4. Quiz Game
5. Treasure Island

### Treasure Island

>`10.02.2023` Currently rebuilding the application to use classes. Treasure Island is in the making.

> `9.27.2023` This game currently has 3 stories in the JSON data file, they all have different names but they are the same story. I duplicated the data for testing and left
> them as-is for demonstration. However, I will be creating some new storylines ASAP!

## File Hierarchy Glossary

### Classes Folder

The Classes directory holds all the main Class files for operating the game, such as `Menu.py` which is the primary application file. These files are accessed and imported during normal gameplay. Each class file acts like a "cartridge" or "game disc" when accessed by the Menu app for different games.

### Modules Folder

The Modules directories store required files for the parent directory files. For example, the `Quiz_Game_Brain.py` is stored in this sub-directory to be used with the `Quiz_Game.py` in the Classes folder.

### Data Folder

The Data directories store any external data file or Python file that is primarily used for behind-the-scenes functions like a JSON file that stores standard game data used for gameplay. It also includes API functions and large string variables like the `rock_paper_scissors_art.py` file which stores the artwork to be displayed during gameplay.
