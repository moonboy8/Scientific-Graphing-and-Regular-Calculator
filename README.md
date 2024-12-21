# Graphing and Scientific Calculator

This is a Python-based calculator application with two distinct functionalities:
1. **Graphing Calculator**: Plot mathematical equations and solve for specific `x` or `y` values.
2. **Scientific Calculator**: Perform scientific and arithmetic calculations, including trigonometric and logarithmic functions.

The application uses the **Tkinter** library for the graphical user interface (GUI) and **Matplotlib** for plotting graphs. It also incorporates **SciPy** for solving equations.

## Features

### Graphing Calculator
- **Equation Input**: Enter mathematical equations in the form `y = f(x)`.
- **Graph Plotting**: Plot the graph of the given equation within the range `x = [-10, 10]`.
- **Find y for x**: Enter a specific `x` value to find the corresponding `y` value.
- **Find x for y**: Enter a specific `y` value to find the corresponding `x` value using numerical solving.

### Scientific Calculator
- **Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Scientific Functions**: Trigonometric functions (`sin`, `cos`, `tan`), logarithmic functions (`log`, `ln`), exponential functions (`exp`), and square root (`sqrt`).
- **Clear and Equals**: Clear the current entry or evaluate the expression.

## Requirements
- Python 3.x
- Tkinter (for the GUI)
- Matplotlib (for graph plotting)
- NumPy (for mathematical functions)
- SciPy (for solving equations)

You can install the required dependencies using `pip`:

```bash
pip install matplotlib numpy scipy
