# Advanced Number Utility

A modern, interactive command-line application for number operations and random number generation with an enhanced user interface.

## Features

- 🧮 **Even Number Calculator**: Calculate the sum of all even numbers up to a given limit
- 🎲 **Random Number Generator**: Generate sets of random numbers with customizable parameters
- 🎯 **Unique Number Generator**: Create collections of non-repeating random numbers
- 🔍 **Number Selector**: Select random subsets from generated number collections
- 🎨 **Enhanced UI**: Color-coded interface with animations and visual formatting
- 🛡️ **Input Validation**: Robust error handling and user input validation

## Requirements

- Python 3.6+
- No external dependencies - built entirely with Python's standard library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bodymohamed01099/Advanced-Number-Utility.git
   cd advanced-number-utility
   ```

2. Run the application:
   ```bash
   python index.py
   ```

## Usage Guide

### Main Menu

When you launch the application, you'll be presented with a menu of options:

1. **Sum of Even Numbers** - Calculate the sum of even numbers up to a specified limit
2. **Random Number Generator** - Generate a list of random numbers
3. **Unique Random Number Generator** - Generate a list of unique random numbers
4. **Select Random Numbers** - Select a subset of random numbers from a larger set
5. **Exit** - Close the application

### Sum of Even Numbers

This feature calculates the sum of all even numbers from 2 up to a specified number.

1. Select option 1 from the main menu
2. Enter a positive number as the upper limit
3. The application will show results calculated using both while and for loop methods

### Random Number Generator

Generate a list of random integers within a specified range.

1. Select option 2 from the main menu
2. Enter how many random numbers you want to generate
3. View the generated list of random numbers

### Unique Random Number Generator

Generate a list of unique random integers (no duplicates).

1. Select option 3 from the main menu
2. Enter how many unique numbers you want to generate
3. Specify the minimum and maximum values for the range
4. View the generated list of unique random numbers

### Select Random Numbers

Create a unique list of numbers, then randomly select a subset from that list.

1. Select option 4 from the main menu
2. Enter how many unique numbers to initially generate
3. Enter how many numbers to randomly select from that list
4. Specify the minimum and maximum values for the range
5. View the selected subset of random numbers

## Code Structure

The application follows object-oriented design principles with three main classes:

- **NumberUtility**: Core functionality for calculations and random number operations
- **UserInterface**: Handles all user interactions and display features
- **NumberApp**: Main application class that connects the UI with utilities

## Technical Details

### Type Annotations

The code uses Python's type hinting system for improved readability and IDE support:

```python
def select_random_numbers(n: int, x: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
```

### Terminal Features

The application uses ANSI color codes to enhance the terminal output:

```python
COLORS = {
    "reset": "\033[0m",
    "red": "\033[91m",
    "green": "\033[92m",
    # ... more colors
}
```

### Cross-Platform Support

The application is designed to work across different operating systems:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built as part of a programming exercise to demonstrate Python coding techniques
- Inspired by educational needs for demonstrating random number generation and summation algorithms
