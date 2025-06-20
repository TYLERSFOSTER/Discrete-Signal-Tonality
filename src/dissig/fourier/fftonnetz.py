"""
Performs discrete Fourier analysis on a Signal instance, and puts resulting
component signals into a Signal-decorated tonnetz
"""
from __future__ import annotations

import numpy as np

from dissig.signals.discrete import Signal, character_signal
from dissig.tonnetze.networks import SignalTonnetz


def fft_with_multipliers(discrete_signal : Signal) -> dict[int, complex]:
    """
    Computes the discrete Fourier transform of a Signal instance.

    Args:
        discrete_signal (Signal): The input signal, assumed to be periodic with a fixed sample count.

    Returns:
        dict[int, complex]: A dictionary mapping each integer multiplier (frequency index)
            to its corresponding Fourier coefficient.
    """
    signal_as_list = discrete_signal.underlying_signal

    fft_output = np.fft.fft(signal_as_list)
    fft_output = fft_output.tolist()

    fft_coeffs = {
        multiplier : coefficient for multiplier,
        coefficient in enumerate(fft_output)
    }

    return fft_coeffs


def fft_tonnetz(discrete_signal : Signal, integer_list : list[int]) -> SignalTonnetz:
    """
    Constructs a SignalTonnetz whose nodes are decorated with the Fourier components
    of the input signal scaled by corresponding character signals.

    Args:
        discrete_signal (Signal): A discrete periodic signal to analyze via Fourier transform.
        integer_list (list[int]): List of multipliers defining the structure of the tonnetz.

    Returns:
        SignalTonnetz: A tonnetz graph where each node's signal is the input signal’s
            Fourier coefficient scaled by a character signal.
    """
    modulus = discrete_signal.sample_count

    generating_character = character_signal(1, modulus)
    signal_tonnetz = SignalTonnetz(generating_character, integer_list, include_zero=True)

    fft_coeffs = fft_with_multipliers(discrete_signal)

    for multiplier in range(modulus):
        current_coefficient = fft_coeffs[multiplier]
        original_signal = signal_tonnetz.network.nodes[multiplier]["signal"]
        original_signal_list = original_signal.underlying_signal

        new_signal_list = [current_coefficient * value for value in original_signal_list]
        weighted_signal = Signal(new_signal_list)

        signal_tonnetz.network.nodes[multiplier]["signal"] = weighted_signal
    
    return signal_tonnetz