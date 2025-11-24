# 🧩 API Reference

This page provides detailed documentation for all public interfaces in the **Probability Calculator** package.

---

# 🎩 `Hat` Class

A container that stores colored balls and allows random draws without replacement.

## 📌 Constructor

```python
Hat(**kwargs)
```

### Parameters
- Each keyword argument represents a **color** and the associated **number of balls**.

Example:
```python
hat = Hat(red=3, blue=2)
```

---

## 🔽 `draw(num_balls)`

Draws a number of balls at random **without replacement**.

### Parameters
- `num_balls` *(int)* — number of balls to draw.

### Returns
A list of strings representing the drawn balls.

### Behavior
- If `num_balls` ≥ total balls, **all** balls are returned.
- Otherwise, a random subset is returned.

Example:
```python
hat.draw(4)
```

---

## 🧵 `__repr__()`

Provides a developer-friendly string representation:

```
Hat(['red', 'blue', 'green'])
```

---

# 🧪 `experiment()` Function

Runs repeated Monte-Carlo trials to estimate the probability of drawing a specific combination of balls.

## 📌 Signature

```python
experiment(hat, expected_balls, num_balls_drawn, num_experiments)
```

---

## Parameters

| Name | Type | Description |
|------|------|-------------|
| **hat** | `Hat` | The original hat object (deep copied internally) |
| **expected_balls** | `dict[str, int]` | Required colors and their minimum counts |
| **num_balls_drawn** | `int` | Number of balls drawn per experiment |
| **num_experiments** | `int` | Number of Monte-Carlo repetitions |

---

## 🔄 Process

1. Deep copy the hat  
2. Draw `num_balls_drawn` balls  
3. Count colors  
4. Check if all expected colors meet/exceed their required counts  
5. Repeat for `num_experiments` trials  
6. Return `successes / num_experiments`

---

## 📤 Returns

A **float** between **0** and **1**, the estimated probability.

Example:
```python
from probability_calculator import Hat, experiment

hat = Hat(black=6, red=4, green=3)

probability = experiment(
    hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=3000
)

print(probability)
```

---

## 🧭 Notes

- The original `hat` is *not modified*  
- More experiments → more accurate results  
- Uses random sampling without replacement  

---

Proceed to **Examples** to see full workflows in action! 🚀
