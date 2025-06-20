import numpy as np
import pytest

from dissig.signals.discrete import Signal, character_signal
from dissig.tonnetze.networks import SignalTonnetz
from dissig.fourier.fftonnetz import fft_with_multipliers, fft_tonnetz


@pytest.mark.parametrize("samples, expected_fft", [
    ([1, 0, 0, 0], [1, 1, 1, 1]),
    ([0, 1, 0, 0], [1, -1j, -1, 1j]),
    ([1, 1, 1, 1], [4, 0, 0, 0]),
    ([1, -1, 1, -1], [0, 0, 4, 0]),
])
def test_fft_with_multipliers(samples, expected_fft):
    signal = Signal([complex(x, 0) for x in samples])
    result = fft_with_multipliers(signal)
    expected = {k: pytest.approx(v, abs=1e-10) for k, v in enumerate(expected_fft)}
    for k in range(len(samples)):
        assert result[k] == expected[k]


@pytest.mark.parametrize("samples, integer_list", [
    ([1, 0, 0, 0], [1, 2]),
    ([1, 1, 1, 1], [1, 3]),
    ([1, -1, 1, -1], [1]),
])
def test_fft_tonnetz_signal_consistency(samples, integer_list):
    signal = Signal([complex(x, 0) for x in samples])
    tonnetz = fft_tonnetz(signal, integer_list)
    modulus = len(samples)

    fft_coeffs = fft_with_multipliers(signal)

    for multiplier in range(modulus):
        coeff = fft_coeffs[multiplier]
        node_signal = tonnetz.network.nodes[multiplier]["signal"]
        node_signal_list = node_signal.underlying_signal

        # Check that this signal is a scalar multiple of the original character signal
        character = character_signal(multiplier, modulus)
        expected_values = [coeff * x for x in character.underlying_signal]
        actual_values = list(node_signal_list)
        for a, b in zip(actual_values, expected_values):
            assert a == pytest.approx(b, abs=1e-10)
