# Internship Projects: Rock-Paper-Scissors Game, Simple Calculator, and Dice Rolling Simulator

## Overview

This repository contains three simple Python projects developed as part of an internship. Each project is designed to demonstrate basic programming concepts and provide user-friendly experiences.

1. **Rock-Paper-Scissors Game**
2. **Simple Calculator**
3. **Dice Rolling Simulator**

## Requirements

- Python 3.x

## Project 1: Rock-Paper-Scissors Game

### Description

This is a simple Rock-Paper-Scissors game where the user plays against the computer. The game tracks the score across multiple rounds and provides clear instructions and feedback.

### Features

- User Input: Select rock, paper, or scissors.
- Computer Selection: Randomly generates the computer's choice.
- Game Logic: Determines the winner based on the rules.
- Display Result: Shows user and computer choices, and the outcome (win, lose, or tie).
- Score Tracking: Records scores for multiple rounds.
- Play Again: Option to play another round.

### Usage

1. Navigate to the directory containing `rock_paper_scissors.py`.
2. Run the script using:
    ```sh
    python rock_paper_scissors.py
    ```

### Code Overview

- `get_user_choice()`: Prompts the user to enter their choice.
- `get_computer_choice()`: Randomly selects the computer's choice.
- `determine_winner(user_choice, computer_choice)`: Determines the winner.
- `display_result(user_choice, computer_choice, result)`: Displays choices and results.
- `play_again()`: Asks if the user wants to play again.
- `main()`: Runs the game loop and handles scoring.

## Project 2: Simple Calculator

### Description

This is a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

### Features

- User Input: Prompt for two numbers and an operation.
- Perform Calculation: Executes the chosen operation.
- Display Result: Shows the result of the calculation.
- Error Handling: Manages invalid inputs and division by zero.

### Usage

1. Navigate to the directory containing `calculator.py`.
2. Run the script using:
    ```sh
    python calculator.py
    ```

### Code Overview

- `add(a, b)`: Returns the sum of `a` and `b`.
- `subtract(a, b)`: Returns the difference between `a` and `b`.
- `multiply(a, b)`: Returns the product of `a` and `b`.
- `divide(a, b)`: Returns the quotient of `a` and `b` or an error message for division by zero.
- `main()`: Handles user input, performs operations, and displays the result.

## Project 3: Dice Rolling Simulator

### Description

This is a simple dice rolling simulator that allows users to specify the number of sides on the dice and the number of rolls. The program generates random numbers for each roll and displays the results.

### Features

- User Input: Specify the number of sides and rolls.
- Dice Rolling Logic: Generates random numbers for each roll.
- Display Results: Shows the outcome of each roll.

### Usage

1. Navigate to the directory containing `dice_roller.py`.
2. Run the script using:
    ```sh
    python dice_roller.py
    ```

### Code Overview

- `roll_dice(num_sides, num_rolls)`: Rolls the dice and returns the results.
- `main()`: Handles user input, performs rolls, and displays the results.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
