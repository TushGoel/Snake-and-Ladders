# Python Board Game

This Python script simulates a board game with chutes (snakes) and ladders. Players roll dice and move on the board, and they can encounter chutes and ladders that affect their progress. The game continues until a player reaches the winning position.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Features](#features)
- [File Structure](#file-structure)

## Installation

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed. This code was written in Python 3.

3. You may need to install the `random` module, which is used for generating random numbers. If it's not already installed, you can install it using pip:

   ```bash
   pip install random
   ```

4. Run the script using a Python interpreter.

## Usage

The script contains three classes: `Rollable`, `Player`, and `Game`.

- `Rollable`: Simulates the rolling of dice. Users can choose from three types of dice: 4-sided, 6-sided, or both.

- `Player`: Represents a player with a name and a location on the board.

- `Game`: Manages the game and player movements on the board. It also handles chutes and ladders, ensuring a player reaches the winning position.

## How to Play

1. Download or create a CSV file describing the game board, with values like "S1", "L1", etc. (snakes and ladders) to represent chutes (snakes) and ladders. The file path should be updated in the code (board_file_path variable) to specify the board configuration.

2. Run the Python script. It will prompt you for the number of players and their names.

3. Choose the type of dice or dices you want to use (4-sided, 6-sided, or both).

4. The game will start, and players will take turns rolling the dice and moving on the board.

5. The game continues until one of the players reaches the winning position (location 100).

## Features

- Supports different types of dice, allowing for various game configurations.

- Handles chutes and ladders on the board, affecting player movements.

- Prevents players from landing on position 99 when using both 4-sided and 6-sided dice either by rolling the dice or climbing the ladder, as this would lead to an infinite loop.

- Provides a clear winner when a player reaches location 100.

## File Structure

- `board1.csv`, `board2.csv`, `board3.csv` : Contains the board configuration/s with chutes (S) and ladders (L).

- `README.md`: This documentation file.

- `game.py`: The Python script for the board game.
