"""
Unit tests for Signal and character_signal in discrete signal module.
"""
from __future__ import annotations

import pytest
import numpy as np

from dissig.signals.discrete import Signal, character_signal


@pytest.mark.parametrize(
    "sample_list",
    [
        [1+0j, -1+0j, 1j],
        [np.exp(1j * 2 * np.pi * t / 4) for t in range(4)],
        [complex(0), complex(1), complex(-1)],
    ]
)
def test_signal_init_valid(sample_list):
    """Test valid Signal initialization."""
    signal = Signal(sample_list)
    assert len(signal) == len(sample_list)
    assert signal.underlying_signal == sample_list
    assert isinstance(signal.ring_units, list)
    assert all(isinstance(u, int) for u in signal.ring_units)


@pytest.mark.parametrize(
    "bad_sample_list",
    [
        [],                            # empty list
        [1.0, 2.0, 3.0],               # not complex
        [1+0j, 2+0j, "not a complex"], # contains invalid type
        None,                          # not a list
    ]
)
def test_signal_init_invalid(bad_sample_list):
    """Test invalid Signal initialization raises assertion."""
    with pytest.raises(AssertionError):
        Signal(bad_sample_list)


@pytest.mark.parametrize(
    "samples, multiplier, expected_indices",
    [
        ([1+0j, 2+0j, 3+0j], 1, [0, 1, 2]),  # identity
        ([1+0j, 2+0j, 3+0j], 2, [0, 2, 1]),  # permutation mod 3
        ([10+0j, 20+0j, 30+0j, 40+0j], 3, [0, 3, 2, 1]),  # reverse mod 4
    ]
)
def test_scale_time_by(samples, multiplier, expected_indices):
    """Test signal time scaling by a multiplier."""
    signal = Signal(samples)
    scaled = signal.scale_time_by(multiplier)
    expected = [samples[i] for i in expected_indices]
    assert scaled.underlying_signal == expected


@pytest.mark.parametrize(
    "samples, query_idx, expected_value",
    [
        ([1+1j, 2+2j, 3+3j], 0, 1+1j),
        ([1+1j, 2+2j, 3+3j], 2, 3+3j),
        ([1+1j, 2+2j, 3+3j], 3, 1+1j),  # mod 3
        ([1+1j, 2+2j, 3+3j], -1, 3+3j), # negative indexing mod 3
    ]
)
def test_forward(samples, query_idx, expected_value):
    """Test forward signal access with modular indexing."""
    signal = Signal(samples)
    assert signal.forward(query_idx) == expected_value


def test_forward_invalid_index_type():
    """Test invalid index type in forward method."""
    signal = Signal([1+0j])
    with pytest.raises(AssertionError):
        signal.forward("not an int") # type: ignore


def test_scale_time_invalid_multiplier():
    """Test invalid multiplier raises assertion in scaling."""
    signal = Signal([1+0j, 2+0j])
    with pytest.raises(AssertionError):
        signal.scale_time_by("bad multiplier") # type: ignore


@pytest.mark.parametrize(
    "multiplier, modulus, expected_length",
    [
        (0, 1, 1),
        (1, 4, 4),
        (2, 6, 6),
        (3, 8, 8),
    ]
)
def test_character_signal(multiplier, modulus, expected_length):
    """Test character_signal properties and output type."""
    result = character_signal(multiplier, modulus)

    # Check length
    assert isinstance(result, Signal)
    assert len(result) == expected_length

    # Check that each entry is a complex number of magnitude 1
    for z in result.underlying_signal:
        assert isinstance(z, complex)
        assert np.isclose(abs(z), 1.0)


@pytest.mark.parametrize(
    "input_values, normalize, expected",
    [
        ([1+2j, 2+0j, -3+1j], False, [1.0, 2.0, -3.0]),
        ([1+2j, 2+0j, -3+1j], True, [1.0/3, 2.0/3, -1.0]),
        ([0j, 0j, 0j], False, [0.0, 0.0, 0.0]),
        ([0j, 0j, 0j], True, [0.0, 0.0, 0.0]),  # no division by zero because of 1e-8
        ([-1-1j, -2-2j, -0.5-0.5j], True, [-0.5, -1.0, -0.25])
    ]
)
def test_extract_real(input_values, normalize, expected):
    """Test real part extraction and optional normalization."""
    signal = Signal(input_values)
    result = signal.extract_real(normalize=normalize)
    assert all(abs(r - e) < 1e-6 for r, e in zip(result, expected))
