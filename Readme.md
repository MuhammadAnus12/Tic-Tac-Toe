# Tic Tac Toe AI

This is a Python-based Tic Tac Toe game with an AI opponent. The AI can use either the Minimax algorithm or the Alpha-Beta Pruning algorithm to make its moves. The game is built using the `pygame` library for the graphical interface.

## Features

- Play Tic Tac Toe against an AI opponent.
- Toggle between Minimax and Alpha-Beta Pruning algorithms during gameplay.
- Restart the game at any time.
- Visual representation of the board and moves.

## Project Structure
aiplayer.py 
# AI player logic 
alphabeta.py 
# Alpha-Beta Pruning algorithm implementation 
board.py 
# Board representation and game logic 
config.py 
# Configuration for colors, dimensions, etc. 
main.py 
# Main game loop and UI logic 
minimax.py 
# Minimax algorithm implementation Readme.md 

# Project documentation

## How to Run

1. Install Python (version 3.10 or higher is recommended).
2. Install the required library:
   ```bash
   pip install pygame

3. Run the game:
   ```bash
   python main.py

Controls
T: Toggle between Minimax and Alpha-Beta Pruning algorithms.
R: Restart the game.
Mouse Click: Make a move by clicking on an empty cell.


How It Works
 The game board is represented as a 3x3 grid.
The human player uses the "O" symbol, and the AI uses the "X" symbol.
The AI calculates the best move using either the Minimax or Alpha-Beta Pruning algorithm, depending on the selected mode.

Algorithms
Minimax
Explores all possible moves to determine the optimal move.
Guarantees the best outcome for the AI but can be slow for larger boards.
Alpha-Beta Pruning
An optimized version of Minimax that eliminates branches that do not need to be explored.
Significantly faster than Minimax for the same board size.