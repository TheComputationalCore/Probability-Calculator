"""
Probability Calculator package.

Provides:
- Hat: container of colored balls
- experiment: Monte-Carlo probability estimator
"""

from .hat import Hat
from .experiment import experiment

__all__ = ["Hat", "experiment"]
