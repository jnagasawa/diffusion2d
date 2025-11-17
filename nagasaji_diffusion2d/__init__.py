"""
nagasaji_diffusion2d

A package for solving the two-dimensional diffusion equation.
"""

from .diffusion2d import solve
from .output import create_plot, output_plots

__version__ = "0.0.1"
__all__ = ["solve", "create_plot", "output_plots"]
