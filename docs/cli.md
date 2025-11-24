# 🖥️ Command Line Interface (CLI)

The Probability Calculator provides a convenient command-line interface that allows you to run Monte‑Carlo probability simulations without writing Python code.

---

## ▶️ Running the CLI

Once installed (`pip install .`), run:

```bash
probability-calculator --help
```

This displays available commands and options.

---

## 🎩 Creating a Hat via CLI

You specify balls using `color=count` pairs:

```bash
probability-calculator --hat red=3 blue=2 green=6
```

This defines a hat with:

- 3 red balls  
- 2 blue balls  
- 6 green balls  

---

## 🔢 Setting Expected Outcome

Specify the expected minimum number of balls of each color:

```bash
--expect red=2 green=1
```

---

## 🎲 Running a Full Simulation

Example:

```bash
probability-calculator \
  --hat red=3 blue=2 green=6 \
  --expect red=2 green=1 \
  --draw 5 \
  --experiments 2000
```

Output:

```
Estimated Probability: 0.2385
```

---

## 📌 CLI Arguments

| Argument | Description |
|---------|-------------|
| `--hat` | Define hat contents as `color=count` pairs |
| `--expect` | Required ball counts for success |
| `--draw` | Number of balls drawn per experiment |
| `--experiments` | Number of Monte‑Carlo repetitions |

---

## 🧠 How It Works

1. Parse colors and counts from CLI  
2. Construct a `Hat` object  
3. Perform repeated draws  
4. Calculate how many experiments meet expectations  
5. Print probability estimate  

---

## 📚 Related Documentation

- [Usage Guide](usage.md)  
- [API Reference](api.md)  
- [Examples](examples.md)

---

Run your first simulation now! 🎲
