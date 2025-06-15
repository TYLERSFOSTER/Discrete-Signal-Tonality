"""
Script for generating transformed signals under tonnetz
"""
from __future__ import annotations

from dissig.signals.discrete import character_signal
from dissig.tonnetze.networks import SignalTonnetz
from dissig.io.print_wav import tonnetz_to_wav

if __name__ == "__main__":
    N = 36
    signal = character_signal(1, 36)
    signal_tonnetz = SignalTonnetz(signal, [2, 3, 5])
    tonnetz_to_wav(signal_tonnetz, 440.0, 1.0)
