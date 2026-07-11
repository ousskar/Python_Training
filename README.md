# Python Training

A hands-on, 3-day Python course for beginners to intermediate learners. Content is organized into numbered folders you work through in order, each with Jupyter notebooks, exercises, and solutions.

## What you'll learn

- **Day 1 — Python Foundations:** syntax, data types, variables, iterables, indexing/slicing, and flow control
- **Day 2 — Functions and Code Organization:** functions, scope, files, modules/packages, OOP, and decorators
- **Day 3 — Testing, Debugging, and Reliability:** unit testing, mocking, pytest, and debugging tools

See [Contents.md](Contents.md) for the full day-by-day breakdown of topics.

## Getting started

1. **Install Python 3.10+** if you don't already have it.
2. **Clone this repo:**
   ```bash
   git clone https://github.com/ousskar/Python_Training.git
   cd Python_Training
   ```
3. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   pip install jupyter pytest
   ```
4. **Launch Jupyter** and open the notebooks in order:
   ```bash
   jupyter notebook
   ```

## How the content is organized

Each folder corresponds to one topic and is meant to be worked through in order:

| Folder | Topic |
| --- | --- |
| `01 - Introduction to Python` | Setup and first scripts |
| `02 - Data Types and Variables` | Numbers, strings, lists, dicts, variables |
| `03 - Iterables, Indexing, and Slicing` | Iterators and sequence slicing |
| `04 - Flow Control` | If/else, loops, comprehensions |
| `05 - Practice Session` | Exercises + a mini data-prep project |
| `06 - Functions` | Functions, scope, args/kwargs, type hints |
| `07 - Working with Files` | File I/O, CSV, JSON |
| `08 - Python Libraries, Modules, and Packages` | Imports, modules, packages |
| `09 - Object-Oriented Programming` | Classes, inheritance, dataclasses |
| `10 - Higher-Order Functions and Decorators` | Lambdas, decorators |
| `11 - Unit Testing` | `unittest`, mocking, `pytest` |
| `12 - Debugging` | Errors, exceptions, debugging tools |
| `13 - Final Practice and Wrap-Up` | Cumulative exercises + LLM capstone project |

Many folders include a `Solutions` subfolder — try the exercises yourself before peeking!

## Tips for students

- Run notebook cells in order; later cells often depend on earlier ones.
- Experiment freely — break things, then figure out why. That's the fastest way to learn.
- If you get stuck, check the `Solutions` folder for that topic, but try for at least 10-15 minutes first.
- Day 3's testing and debugging skills apply to everything you wrote on Days 1-2, so revisit earlier exercises once you've learned them.
