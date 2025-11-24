# ============================
#  Probability Calculator — Makefile
# ============================

PYTHON=python3

# ----------------------------
#  Code Quality
# ----------------------------

lint:
	flake8 .

format:
	black .

check-format:
	black --check .

# ----------------------------
#  Testing
# ----------------------------

test:
	pytest -q

# ----------------------------
#  Documentation
# ----------------------------

docs:
	mkdocs serve

build-docs:
	mkdocs build

deploy-docs:
	mkdocs gh-deploy --force

# ----------------------------
#  Installation
# ----------------------------

install:
	pip install -e .

# ----------------------------
#  Utility
# ----------------------------

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache build dist *.egg-info site

all: format lint test
