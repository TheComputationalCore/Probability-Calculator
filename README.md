# 🎲 Probability Calculator

A Python module for simulating the probability of drawing specific combinations of colored balls from a hat.  
Uses Monte‑Carlo simulation to estimate probabilities.

---

## 📦 Features

- 🎩 **Hat class** for creating bags of colored balls  
- 🔀 Random drawing **without replacement**  
- 📊 Monte‑Carlo probability estimation (`experiment`)  
- 🧪 Fully customizable simulations  
- 🖥️ **Command Line Interface** (`probability-calculator`)  
- 🧾 Detailed documentation (MkDocs Material)  
- ✔️ Fully tested and linted (pytest, flake8, black)

---

## 🚀 Installation

Clone and install:

```bash
git clone https://github.com/TheComputationalCore/Probability-Calculator.git
cd Probability-Calculator
pip install .
```

---

## 🎩 Basic Usage

### Create a hat

```python
from probability_calculator import Hat

hat = Hat(red=3, blue=2, green=6)
print(hat.contents)
```

### Draw balls

```python
drawn = hat.draw(4)
print(drawn)
```

### Run a probability experiment

```python
from probability_calculator import experiment

prob = experiment(
    hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(prob)
```

---

## 🖥️ CLI Usage

Run directly from the terminal:

```bash
probability-calculator --hat red=3 blue=2 green=6 --expect red=2 green=1 --draw 5 --experiments 2000
```

Output example:

```
Estimated Probability: 0.2385
```

---

## 📚 Documentation

Full documentation is available at:

➡️ **https://thecomputationalcore.github.io/Probability-Calculator**

Includes:

- Usage Guide  
- API Reference  
- CLI Guide  
- Examples  
- Contribution Guide  

---

## 🧪 Running Tests

```bash
pytest -q
```

---

## 🧼 Code Quality

The repo uses:

- **Black** — code formatter  
- **Flake8** — linter  
- **pytest** — tests  

GitHub Actions automatically run:

- Lint checks  
- Tests  
- Docs deployment  

---

## 🤝 Contributing

Contributions are welcome!  
Please read: **CONTRIBUTING.md**

---

## 🛡 Security

See: **SECURITY.md**  
## ✉️ Contact

**Dinesh Chandra — TheComputationalCore**  
- GitHub: https://github.com/TheComputationalCore 

---

## 📄 License

Released under the **MIT License**.

---


