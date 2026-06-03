# ❌ AI Unbeatable Tic-Tac-Toe ⭕

A command-line Tic-Tac-Toe game written in Python. Play against a computer opponent driven by a recursive **Minimax algorithm** that calculates every possible outcome to ensure it never loses!

---

## 🎮 How to Play

The game is played on a 3x3 grid. The grid squares are mapped to numbers `1` through `9` as shown below:

 1 | 2 | 3
 --|---|---
 4 | 5 | 6
 --|---|---
 7 | 8 | 9
 

1. You play as **X** and always go first.
2. Type a number from `1-9` to choose your spot and press `Enter`.
3. The computer will analyze the board and instantly make its optimal move as **O**.
4. The game ends when a player gets 3 in a row (horizontally, vertically, or diagonally) or when the board is full (a draw).

---

## 🤖 How the AI Works (Minimax)

The backbone of the computer's strategy is the **Minimax Decision Algorithm**. 
* **Lookahead:** The AI plays out every single possible variation of the game right down to the final move.
* **Scoring:** It assigns a score to every final board state: a high positive score if the computer wins, and a low negative score if the human wins.
* **Optimization:** It backtracks up the decision tree, choosing the path that maximizes its own score while assuming you will play perfectly to minimize it. 

Because it maps out the entire game state tree, **the AI is mathematically unbeatable**. The best result a human player can achieve is a draw!

---

## 🛠️ Requirements & Installation

No external libraries or packages are required to run this game. You only need Python installed on your machine.

1. **Clone or Download** this repository.
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the following command:
   ```bash
   python tictactoe.py
