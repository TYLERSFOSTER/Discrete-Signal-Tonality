"""
./src/dissig/utils/print_sound.py

This script provides functionality for converting a complex-valued signal
to a 16-bit PCM WAV audio file by extracting and normalizing the real part
of the signal.

The main function, `to_wav`, performs the following steps:
- Extracts the real part of the complex signal.
- Normalizes the signal to fit within [-1, 1].
- Resamples it to match a specified WAV sample rate and duration.
- Scales the signal to 16-bit integer range and writes it as a `.wav` file.

The output file is saved under `results/wav_files/` in the project root.

Dependencies:
- numpy
- scipy.io.wavfile
- math
- pathlib
"""
from __future__ import annotations

from pathlib import Path

import math
from scipy.io import wavfile
import numpy as np

from dissig.signals.discrete import Signal


MAX_INT16 = np.iinfo(np.int16).max # maximum value for a signed 16-bit integer


def to_wav(
    signal: Signal,
    signal_max_freq: float,
    wav_duration: float,
    wav_sample_rate: int = 44100,
    filename: str = "test_signal"
) -> None:
    """
    Prints an instance of the Signal class by saving it as a WAV file.

    The function extracts the real part of the complex signal, normalizes it to the range [-1, 1],
    resamples it at the given WAV sample rate for the specified duration, and writes the resulting
    waveform to a 16-bit WAV file.

    Args:
        signal (Signal): The input complex-valued signal object, expected to support `extract_real(normalize=True)`.
        signal_max_freq (float): The maximum frequency of the signal in Hz. Used to calculate the signal's sample period.
        wav_duration (float): The desired duration of the output WAV file in seconds.
        wav_sample_rate (int, optional): The sampling rate of the output WAV file. Defaults to 44100 Hz.
        filename (str, optional): The base name for the output WAV file (without extension). Defaults to "test_signal".

    Raises:
        AssertionError: If `signal_max_freq` is not a positive float, or if `wav_sample_rate` is not a positive integer.

    Side Effects:
        Writes a `.wav` file to the directory `results/wav_files/` under the project root.
    """
    assert isinstance(signal_max_freq, float)
    assert signal_max_freq > 0
    assert isinstance(wav_sample_rate, int)
    assert wav_sample_rate > 0

    N = len(signal)

    normalized_real_signal = signal.extract_real(normalize=True)

    wave_sample_period = 1 / wav_sample_rate
    signal_sample_period = 1 / signal_max_freq

    resampled_ostinato = []
    wav_sample_count = math.floor(wav_duration * wav_sample_rate)
    for wav_sample_idx in range(wav_sample_count):
        signal_sample_index = math.floor(wav_sample_idx * wave_sample_period / signal_sample_period)
        signal_sample_index = signal_sample_index%N

        value = normalized_real_signal[signal_sample_index]
        resampled_ostinato.append(value)

    resampled_waveform = np.array(resampled_ostinato)
    rescaled_waveform = resampled_waveform * MAX_INT16
    int_waveform = rescaled_waveform.astype(np.int16)
    
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    output_dir = project_root / "results" / "wav_files"
    output_dir.mkdir(parents=True, exist_ok=True)

    save_path = output_dir / f"{filename}.wav"

    wavfile.write(save_path, wav_sample_rate, int_waveform)