# Probability Calculator

## Overview
This project implements a Probability Calculator in Python to estimate the probability of drawing specific combinations of colored balls from a hat. It uses object-oriented programming with a `Hat` class and an `experiment` function to simulate random draws without replacement and calculate empirical probabilities.

## Features
- **Hat Class**:
  - Initialize with keyword arguments specifying ball colors and counts (e.g., `Hat(red=5, blue=2)`).
  - Stores balls in a `contents` list, where each ball is represented by a string of its color.
  - Method: `draw(num_balls)` to randomly draw and remove balls from the hat, returning them as a list.
- **Experiment Function**:
  - Takes a `Hat` object, expected balls (dictionary), number of balls to draw, and number of experiments.
  - Returns the probability of drawing at least the specified balls based on multiple experiments.
- **Functionality**:
  - Simulates random draws without replacement.
  - Uses deep copying to preserve the original hat.
  - Handles cases where the number of balls drawn exceeds the hat's contents.
  - Provides approximate probabilities through repeated experiments.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/thesoulseizure/probability-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd probability-calculator
   ```
3. Ensure Python 3.x is installed:
   ```bash
   python --version
   ```

## Usage
Here's an example of how to use the `Hat` class and `experiment` function:

```python
from main import Hat, experiment

# Create a hat with 6 black, 4 red, and 3 green balls
hat = Hat(black=6, red=4, green=3)

# Define expected balls to draw (at least 2 red and 1 green)
expected_balls = {"red": 2, "green": 1}

# Run experiment: draw 5 balls, 2000 times
probability = experiment(
    hat=hat,
    expected_balls=expected_balls,
    num_balls_drawn=5,
    num_experiments=2000
)
print(probability)  # Output: ~0.356 (varies due to randomness)

# Example with different configuration
hat2 = Hat(blue=5, red=4, green=2)
expected_balls2 = {"red": 1, "green": 2}
probability2 = experiment(
    hat=hat2,
    expected_balls=expected_balls2,
    num_balls_drawn=4,
    num_experiments=2000
)
print(probability2)  # Output: ~0.1 (varies due to randomness)
```

## Testing
The code has been tested to meet the following requirements:
1. Correct initialization of the `Hat` object with specified ball counts in `contents`.
2. The `draw` method reduces the number of balls in `contents`.
3. The `draw` method returns all balls when the number of balls to draw exceeds the hat's contents.
4. The `experiment` function returns an approximate probability that varies with each run due to randomness.

To run tests, use the example code above in a Python environment. Open the browser console (F12) to see verbose test output if running in a compatible environment.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the existing style and passes all tests.
