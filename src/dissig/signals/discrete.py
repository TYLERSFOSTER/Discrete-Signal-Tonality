"""
dissig.signal.discrete

This module defines the `Signal` class, representing a finite-length discrete-time signal.
It includes modular time-domain operations and utility constructors for real and character signals.
"""
from __future__ import annotations

import numpy as np

from dissig.utils.arithmetic import multiplicative_units

class Signal():
    """
    A discrete-time, finite-length signal represented by a list of complex-valued samples.

    Attributes:
        sample_count (int): Number of samples in the signal.
        underlying_signal (list[complex]): The signal values.
        ring_units (list[int]): Multiplicative units in ℤ/sample_countℤ.
    """
    def __init__(self, sample_list : list[complex]):
        """
        Constructs a Signal object from a list of complex samples.

        Args:
            sample_list (list[complex]): Non-empty list of complex numbers.

        Raises:
            AssertionError: If the input is not a list of complex numbers or is empty.
        """
        assert isinstance(sample_list, list)
        assert len(sample_list) >= 1
        assert all(isinstance(entry, complex) for entry in sample_list)

        self.sample_count = len(sample_list)
        self.underlying_signal = sample_list

        self.ring_units = multiplicative_units(self.sample_count)

    def scale_time_by(self, multiplier : int) -> Signal:
        """
        Return a new signal with time rescaled modularly by the given multiplier.

        This performs modular index mapping t ↦ multiplier · t mod N, where N is the signal length.

        Args:
            multiplier (int): Integer multiplier to apply in ℤ/Nℤ.

        Returns:
            Signal: The rescaled signal.

        Raises:
            AssertionError: If the multiplier is not an integer.
        """
        assert isinstance(multiplier, int)

        new_sample_list = [
            self.underlying_signal[(multiplier * idx)%len(self)]
            for idx in range(self.sample_count)
        ]

        new_signal = Signal(new_sample_list)

        return new_signal

    def __len__(self):
        """Return the number of samples in the signal."""
        return self.sample_count

    def forward(self, idx : int) -> complex:
        """
        Retrieve the value at index `idx` modulo the signal length.

        Args:
            idx (int): Index to access (wrapped mod N).

        Returns:
            complex: Sample value at the modular index.

        Raises:
            AssertionError: If idx is not an integer.
        """
        assert isinstance(idx, int)

        value = self.underlying_signal[idx%len(self)]

        return value


    def extract_real(self, normalize=False) -> list[float]:
        """
        Extracts the real parts of the complex-valued signal.

        If `normalize` is True, the real values are scaled to the range [-1, 1]
        by dividing each value by the peak absolute value in the signal.

        Returns:
            list[float]: The list of real parts from the underlying signal,
                        optionally normalized.
        """
        real_signal = [float(value.real) for value in self.underlying_signal]

        max_real_value = max(real_signal)
        min_real_value = min(real_signal)
        peak_value = max(max_real_value, abs(min_real_value))

        if normalize:
            real_signal = [float(value/(peak_value + 1e-8)) for value in real_signal]

        return real_signal


def character_signal(multiplier : int, N : int) -> Signal:
    """
    Construct a character signal from the exponential character
        χ(t) = exp(2πi · multiplier · t / N).

    Args:
        multiplier (int): Frequency multiplier.
        N (int): Signal length; must be ≥ 1.

    Returns:
        Signal: A complex exponential signal of length N.

    Raises:
        AssertionError: If N < 1 or inputs are not integers.
    """
    assert isinstance(multiplier, int)
    assert isinstance(N, int)
    assert N >= 1

    theta = multiplier * (2 * np.pi / N)

    sample_list = [complex(np.exp(complex(0,1) * theta * idx)) for idx in range(N)]

    output_signal = Signal(sample_list)

    return output_signal


def signal_from_real(sample_list : list[int | float]) -> Signal:
    """
    Construct a complex-valued Signal from a list of real numbers.

    Args:
        sample_list (list[int | float]): Real-valued samples.

    Returns:
        Signal: Signal with samples cast as complex numbers (imaginary part 0).
    """
    complexified_sample_list = [complex(value, 0) for value in sample_list]

    resulting_signal = Signal(complexified_sample_list)

    return resulting_signal
