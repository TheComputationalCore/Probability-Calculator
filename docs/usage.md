# 📘 Usage Guide

This guide explains how to use the **Probability Calculator** to simulate drawing colored balls from a hat and estimate probabilities using Monte‑Carlo experiments.

---

## 🎩 Creating a Hat

Create a hat by specifying colors and counts:

```python
from probability_calculator import Hat

hat = Hat(red=3, blue=2, green=6)
print(hat.contents)
# ['red', 'red', 'red', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green']
```

Each keyword argument becomes that many balls inside the hat.

---

## 🔀 Drawing Balls

Draw a specific number of balls *without replacement*:

```python
drawn = hat.draw(4)
print(drawn)
# Example: ['green', 'red', 'blue', 'green']
```

If you try to draw more balls than the hat contains:

```python
hat.draw(50)
```

It simply returns all remaining balls.

---

## 🧪 Running Experiments

Use the `experiment()` function to run repeated Monte‑Carlo trials.

```python
from probability_calculator import experiment, Hat

hat = Hat(red=3, blue=2, green=6)

prob = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)

print(prob)  # Example: 0.2385
```

### 📌 Parameters

| Parameter | Type | Description |
|----------|------|-------------|
| `hat` | Hat | Original hat instance |
| `expected_balls` | dict | Required colors + counts |
| `num_balls_drawn` | int | Balls to draw each experiment |
| `num_experiments` | int | Monte‑Carlo repetitions |

---

## 📈 Interpreting Results

The returned value is a **probability estimate** between **0** and **1**:

- `0.0` → expected balls *almost never* appear  
- `1.0` → expected balls *almost always* appear  
- Between → approximate likelihood from repeated trials  

More experiments = higher accuracy:

```python
experiment(..., num_experiments=10000)
```

---

## 🧹 Important Notes

- The original `hat` is *not* modified — deep copies are used internally.  
- Drawing is always random and without replacement.  
- More balls drawn → greater variance in outcomes.  
- For deterministic testing, seed the RNG:

```python
import random
random.seed(42)
```

---

Next, visit the **API Reference** or explore **Examples** for complete workflows.

