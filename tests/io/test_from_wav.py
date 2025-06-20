import pytest
from unittest.mock import patch
import numpy as np

from dissig.signals.discrete import Signal
from dissig.io.from_wav import read_wav_to_signal

wav_data = [
    ("test_file_1.wav", [1, 2, 3, 4], 44100),
    ("test_file_2.wav", [5, 6, 7, 8, 9], 48000),
    ("test_file_3.wav", [10, 20, 30], 22050),
]

@pytest.mark.parametrize("file_path, samples, sample_rate", wav_data)
def test_read_wav_to_signal(file_path, samples, sample_rate):
    with patch('scipy.io.wavfile.read') as mock_read:
        mock_read.return_value = (sample_rate, np.array(samples))

        signal, rate = read_wav_to_signal(file_path)
        expected_samples = [complex(s, 0) for s in samples]

        assert rate == sample_rate
        assert signal.underlying_signal == expected_samples
