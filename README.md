# Two Player Game
Created by Olaf Böckmann, Evelyn Hoffarth, Paul Kohler, Max Thannheimer, and lots of prompts for VSCode/GitHub Copilot in the course "Generative AI" by Frank Müller.

## Overview
This is a two-player game where each player is represented as a ball on the screen. One player has a mouth on one side of the ball and can chase the other player. The objective is for the player with the mouth to "eat" the other player. Additionally, the game includes a "HAMBURGERS" mode where players can collect hamburgers for extra points.

## Project Structure
```
two-player-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game_logic.py    # Contains the main game logic
│   ├── player.py        # Defines the Player class
│   └── assets
│       └── __init__.py  # Marks the assets directory as a package
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Requirements
To run this game, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Game
To start the game, run the following command in your terminal:

```
python src/main.py
```

## Controls
- Player 1 (Chaser): Use the `W`, `A`, `S`, `D` keys to move.
- Player 2 (Chased): Use the arrow keys to move.

## Gameplay
### NORMAL Mode
- The player with the mouth (Player 1) must chase and eat Player 2.
- When Player 1 successfully "eats" Player 2, Player 2 will disappear from the screen, and Player 1 will gain points.

### HAMBURGER Mode
- In this mode, small hamburgers randomly spawn on the field.
- When a player touches a hamburger, it disappears, and the player gains 0.5 points.
- The game continues with the same chasing mechanics as NORMAL mode.

### Score Display
- When a player scores, a message is displayed in the center of the screen for 0.5 seconds, showing which player scored and how many points they earned.

## Title Screen
- The game starts with a title screen where you can choose between two modes:
  - **NORMAL Mode**: Press `SPACE` to start the game in NORMAL mode.
  - **HAMBURGER Mode**: Press `ENTER` to start the game in HAMBURGER mode.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!