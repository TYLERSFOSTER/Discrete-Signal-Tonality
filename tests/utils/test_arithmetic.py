from __future__ import annotations

import pytest
import math

from dissig.utils.arithmetic import unit_vectors


@pytest.mark.parametrize(
    "N,expected_first_angle,expected_last_angle",
    [
        (1, math.pi / 2, math.pi / 2),
        (2, math.pi / 2, math.pi / 2 - math.pi / 2),
        (4, math.pi / 2, math.pi / 2 - 3 * math.pi / 4),
    ]
)
def test_unit_vectors_angles(N, expected_first_angle, expected_last_angle):
    vectors = unit_vectors(N)
    angles = [math.atan2(y, x) for x, y in vectors]

    assert len(vectors) == N
    assert math.isclose(angles[0], expected_first_angle, abs_tol=1e-9)
    assert math.isclose(angles[-1], expected_last_angle, abs_tol=1e-9)


@pytest.mark.parametrize("N", [1, 2, 3, 5, 10, 20])
def test_unit_vectors_lengths(N):
    vectors = unit_vectors(N)
    for x, y in vectors:
        length = math.sqrt(x**2 + y**2)
        
        assert math.isclose(length, 1.0, rel_tol=1e-9)
