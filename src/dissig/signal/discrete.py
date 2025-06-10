"""
dissig.signal.discrete: class representing a discrete audio signal.
"""
from __future__ import annotations

import math

import torch

class Signal():
    def __init__(self, sample_list : list[float]):
        assert len(sample_list) >= 1
        assert isinstance(sample_list, list)
        assert all([isinstance(entry, float) for entry in sample_list])

        self.sample_count = len(sample_list)
        self.underlying_signal = torch.Tensor(sample_list)

        self.ring_units = [
            sample_number
            for sample_number in range(self.sample_count)
            if math.gcd(sample_number, self.sample_count) == 1
        ]

