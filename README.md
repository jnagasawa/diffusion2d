# nagasaji_diffusion2d

A Python package for solving the two-dimensional diffusion equation using finite difference methods.

<!-- ## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/). -->

## Description

This package solves the two-dimensional diffusion equation on a square domain. The solver uses forward-difference in time and central-difference in space to propagate the solution. The package includes visualization tools to plot the temperature distribution at different time steps.

The diffusion equation is solved for a square plate with initial conditions consisting of a cold background temperature and a hot circular disc at the center. The solver computes the heat diffusion over time using the thermal diffusivity parameter.

## Installing the package

You can install the package using pip:

```bash
pip install nagasaji_diffusion2d
```

Or install from source:

```bash
git clone https://github.com/nagasaji/diffusion2d.git
cd diffusion2d
pip install .
```

## Running this package

After installation, you can use the package in your Python code:

```python
from nagasaji_diffusion2d import solve

# Run with default parameters
solve()

# Run with custom parameters
solve(dx=0.3, dy=0.3, D=6.0)
```

The `solve()` function accepts the following parameters:
- `dx`: Grid spacing in x-direction (default: 0.1 mm)
- `dy`: Grid spacing in y-direction (default: 0.1 mm)
- `D`: Thermal diffusivity (default: 4.0 mm²/s)

## Citing


