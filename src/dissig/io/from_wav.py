"""
Load WAV file as Signal object
"""
from __future__ import annotations

import numpy as np
from scipy.io import wavfile

from dissig.signals.discrete import Signal

def read_wav_to_signal(file_path : str) -> tuple[Signal, int]:
    """
    Import WAV file and convert to instance of Signal class, returning
    Signal instance and sample rate

    Args:
        file_path (str): Path of WAV file to import

    Return:
        Tuple consisting of Signal (generated from WAV) and WAV sample rate
    """
    sample_rate, samples = wavfile.read(file_path)

    complex_samples = [complex(sample, 0) for sample in samples]
    
    discrete_signal = Signal(complex_samples)

    return discrete_signal, sample_rate

