# Contributing to Probability Calculator

Thank you for your interest in contributing!  
This document explains the workflow, guidelines, and best practices for contributing to the **Probability Calculator** project.

---

## 🧱 How to Contribute

### **1. Fork the Repository**
Click **Fork** in the upper-right corner of the GitHub page.

### **2. Clone Your Fork**
```bash
git clone https://github.com/<your-username>/Probability-Calculator.git
cd Probability-Calculator
```

### **3. Create a Feature Branch**
```bash
git checkout -b feature-name
```

### **4. Install the Project in Development Mode**
```bash
pip install -e .
```

### **5. Run Tests**
Make sure everything is passing before making changes:

```bash
pytest -q
```

### **6. Make Your Changes**
Follow project conventions and maintain clean, readable code.

### **7. Format & Lint**
We use **Black** and **Flake8**:

```bash
black .
flake8 .
```

(These also run automatically in GitHub Actions.)

### **8. Commit Your Work**
```bash
git commit -m "Description of your feature or fix"
```

### **9. Push and Open a Pull Request**
```bash
git push origin feature-name
```

Then, open a Pull Request on GitHub.

---

## 🧪 Tests

All new features should include tests under:

```
tests/
```

Run tests locally using:

```bash
pytest -q
```

---

## 🎨 Code Style

We follow:

- **Black** — automatic code formatter  
- **Flake8** — python linter  
- **PEP 8** — Python style guide  

Your code should pass both before submission.

---

## 🔐 Security

If you discover a security issue, **do not** open a public issue.  
Instead, email:

📧 **dineshchandra962@gmail.com**

We will respond promptly.

---

## 💬 Questions?

Feel free to open a discussion or issue on GitHub.

Thank you for helping improve the project! 🚀
