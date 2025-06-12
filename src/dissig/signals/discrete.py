"""
dissig.signal.discrete

This module defines the `Signal` class, representing a finite-length discrete audio signal.
It provides basic arithmetic and structural operations, including modular time scaling.
"""
from __future__ import annotations

import numbers
import math

from dissig.utils.arithmetic import multiplicative_units

class Signal():
    """
    A class representing a discrete-time, finite-length signal as a list of numeric samples.

    Attributes:
        sample_count (int): The total number of samples in the signal.
        underlying_signal (list[float]): The list of signal sample values.
        ring_units (list[int]): List of integers in ℤ/sample_countℤ that are coprime to sample_count.
    """
    def __init__(self, sample_list : list[float]):
        """
        Initialize a Signal from a list of numeric samples.

        Args:
            sample_list (list[float]): A non-empty list of numeric values representing signal samples.

        Raises:
            AssertionError: If sample_list is not a list of numbers or is empty.
        """
        assert len(sample_list) >= 1
        assert isinstance(sample_list, list)
        assert all([isinstance(entry, numbers.Number) for entry in sample_list])

        self.sample_count = len(sample_list)
        self.underlying_signal = sample_list

        self.ring_units = multiplicative_units(self.sample_count)

    def scale_time_by(self, multiplier : int) -> Signal:
        """
        Return a new signal with its time axis scaled modularly by the given integer multiplier.

        This operation is equivalent to resampling the signal by applying a modular
        transformation to the sample indices: t ↦ multiplier * t mod N.

        Args:
            multiplier (int): The integer multiplier to apply to the time axis.

        Returns:
            Signal: A new Signal object with time scaled by the given multiplier.

        Raises:
            AssertionError: If multiplier is not an integer.
        """
        assert isinstance(multiplier, int)

        new_sample_list = [
            self.underlying_signal[(multiplier * idx)%self.sample_count]
            for idx in range(self.sample_count)
        ]

        new_signal = Signal(new_sample_list)

        return new_signal