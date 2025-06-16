"""
Script for generating transformed signals under tonnetz
"""
from __future__ import annotations

from dissig.signals.discrete import character_signal
from dissig.tonnetze.networks import SignalTonnetz
from dissig.io.print_wav import tonnetz_to_wav

if __name__ == "__main__":
    modulus = 45
    integer_list = [2,3, 5]

    signal = character_signal(1, modulus)
    signal_tonnetz = SignalTonnetz(signal, integer_list)

    tonnetz_to_wav(signal_tonnetz, 880.0, 1.0, filename="whaaa")
