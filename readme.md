# Rock-Paper-Scissors

A simple command-line Rock-Paper-Scissors game in Python. The first player (user or computer) to reach **10** points is declared the winner.

## Features
- **Simple Command-Line Interface**  
  Choose between Rock, Paper, Scissors, or Quit.
- **Score Tracking**  
  Displays both user and computer scores on each turn.
- **Win Condition**  
  Automatically ends the game when either you or the computer reaches 10 points.
- **Replay**  
  After each round, press Enter to continue playing until someone wins or you quit.

## How It Works
1. **User Chooses**:
   - **1** for Rock  
   - **2** for Paper  
   - **3** for Scissors  
   - **4** to Quit the game  
2. **Computer Randomly Selects** Rock, Paper, or Scissors using a random integer between 1 and 3.
3. **Points Awarded** based on the outcome:
   - Win = +1 to the user’s score
   - Lose = +1 to the computer’s score
   - Tie = No change in scores
4. Once **10 points** is reached by either the user or computer, the game ends and declares the winner.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. **Clone or Download** this repository.
2. Open a terminal (or command prompt) in the project folder.
3. Run:
   ```bash
   python main.py
