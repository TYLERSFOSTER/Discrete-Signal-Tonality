from __future__ import annotations

import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from pathlib import Path
from scipy.io import wavfile

from dissig.io.print_wav import signal_to_wav, tonnetz_to_wav

class DummySignal:
    def __init__(self, data):
        self.underlying_signal = data

    def extract_real(self, normalize=False):
        real = [float(x.real) for x in self.underlying_signal]
        if normalize:
            peak = max(max(real), abs(min(real))) + 1e-8
            return [r / peak for r in real]
        return real

    def __len__(self):
        return len(self.underlying_signal)


@pytest.mark.parametrize(
    "signal_data, signal_max_freq, wav_duration, wav_sample_rate",
    [
        ([1+0j] * 10, 10.0, 0.01, 8000),
        ([1+1j, -1-1j] * 5, 5.0, 0.02, 16000),
        ([np.exp(1j * 2 * np.pi * t / 20) for t in range(20)], 20.0, 0.05, 44100),
    ]
)
def test_signal_to_wav_creates_file(signal_data, signal_max_freq, wav_duration, wav_sample_rate):
    filename = "pytest_generated_test_signal"
    signal = DummySignal(signal_data)

    # Run the function
    signal_to_wav(signal, signal_max_freq, wav_duration, wav_sample_rate, filename) # type: ignore

    # Reproduce exact logic from the script to compute output path
    test_file = Path(__file__).resolve()
    repo_root = test_file.parent.parent.parent  # up from tests/utils/ to repo root
    save_path = repo_root / "results" / "wav_files" / f"{filename}.wav"

    assert save_path.exists(), f"{save_path} was not created."

    rate, data = wavfile.read(save_path)

    assert rate == wav_sample_rate
    assert data.dtype == np.int16
    assert len(data) == int(wav_duration * wav_sample_rate)

    # Optional cleanup (comment out if you want to inspect the file)
    save_path.unlink()


@pytest.mark.parametrize(
    "node_ids, signal_max_freq, wav_duration, wav_sample_rate, filename",
    [
        ([0, 1, 2], 800.0, 1.0, 22050, "output_A"),
        ([42], 440.0, 0.5, 44100, "solo_node"),
        ([], 880.0, 2.0, 16000, "empty_test"),
    ]
)
def test_tonnetz_to_wav_calls_signal_to_wav(
    node_ids, signal_max_freq, wav_duration, wav_sample_rate, filename
):
    # Create mock signal and SignalTonnetz object
    mock_signal = MagicMock(name="MockSignal")
    mock_network = MagicMock()
    mock_network.nodes = {i: {'signal': mock_signal} for i in node_ids}
    mock_signal_tonnetz = MagicMock()
    mock_signal_tonnetz.network = mock_network

    with patch("dissig.io.print_wav.signal_to_wav") as mock_signal_to_wav:
        tonnetz_to_wav(
            signal_tonnetz=mock_signal_tonnetz,
            signal_max_freq=signal_max_freq,
            wav_duration=wav_duration,
            wav_sample_rate=wav_sample_rate,
            filename=filename,
        )

        # Assert expected number of calls
        assert mock_signal_to_wav.call_count == len(node_ids)

        # Verify call args if there are any nodes
        for i in node_ids:
            mock_signal_to_wav.assert_any_call(
                mock_signal,
                signal_max_freq,
                wav_duration,
                wav_sample_rate=wav_sample_rate,
                filename=f"signal_tonnetz/{filename}_{i}",
            )
