# Two Player Game

## Overview
This is a two-player game where each player is represented as a ball on the screen. One player has a mouth on one side of the ball and can chase the other player. The objective is for the player with the mouth to "eat" the other player.

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
- The player with the mouth (Player 1) must chase and eat Player 2.
- When Player 1 successfully "eats" Player 2, Player 2 will disappear from the screen.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!