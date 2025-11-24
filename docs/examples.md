# 📘 Examples

This page provides complete examples demonstrating how to use the **Probability Calculator** for simulations and probability estimation.

---

## 🎩 Example 1 — Create a Hat and Draw Balls

```python
from probability_calculator import Hat

hat = Hat(red=3, blue=2, green=6)

print("Initial contents:", hat.contents)
drawn = hat.draw(4)

print("Drawn balls:", drawn)
print("Remaining:", hat.contents)
```

**Example output:**
```
Initial contents: ['red', 'red', 'red', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green']
Drawn balls: ['green', 'red', 'green', 'blue']
Remaining: ['red', 'red', 'blue', 'green', 'green', 'green', 'green']
```

---

## 🧪 Example 2 — Run a Probability Experiment

```python
from probability_calculator import Hat, experiment

hat = Hat(red=3, blue=2, green=6)

prob = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print("Estimated probability:", prob)
```

**Example output:**
```
Estimated probability: 0.2385
```

---

## 🔄 Example 3 — Use Random Seed for Reproducibility

```python
import random
from probability_calculator import Hat, experiment

random.seed(42)

hat = Hat(yellow=5, blue=4, red=3)

prob = experiment(
    hat,
    expected_balls={"yellow": 2, "blue": 1},
    num_balls_drawn=4,
    num_experiments=500
)

print(prob)
```

---

## 🎯 Example 4 — CLI Usage (Command Line)

After installation (`pip install .`), run:

```bash
probability-calculator --hat red=3 blue=2 green=6 --expect red=2 green=1 --draw 5 --experiments 2000
```

Example output:

```
Estimated Probability: 0.2385
```

---

## 📊 Example 5 — Large Simulation

```python
from probability_calculator import Hat, experiment

hat = Hat(red=8, blue=5, green=7, yellow=10)

prob = experiment(
    hat,
    expected_balls={"yellow": 3, "red": 2},
    num_balls_drawn=6,
    num_experiments=10000
)

print("Probability:", prob)
```

---

Explore more by checking the **Usage Guide** or **API Reference**. Happy simulating! 🎲
