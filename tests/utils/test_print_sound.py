import pytest
import numpy as np
from pathlib import Path
from scipy.io import wavfile

from dissig.utils.print_sound import to_wav


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
def test_to_wav_creates_file(signal_data, signal_max_freq, wav_duration, wav_sample_rate):
    filename = "pytest_generated_test_signal"
    signal = DummySignal(signal_data)

    # Run the function
    to_wav(signal, signal_max_freq, wav_duration, wav_sample_rate, filename) # type: ignore

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
