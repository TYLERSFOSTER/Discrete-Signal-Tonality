# src/dissig/__init__.py
from __future__ import annotations

# from .core import DissigEngine
from .signals.discrete import Signal
from .utils.primes import primes_below

__all__ = [
    "Signal",
    "primes_below",
]
