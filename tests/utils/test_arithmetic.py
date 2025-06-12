from __future__ import annotations

import pytest
import math

from dissig.utils.arithmetic import unit_vectors, unit_clusters, multiplicative_units


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

@pytest.mark.parametrize(
    "N,expected",
    [
        (1, [0]),           # gcd(0, 1) = 1
        (2, [1]),           # gcd(1, 2) = 1
        (3, [1, 2]),        # gcd(1, 3), gcd(2, 3)
        (4, [1, 3]),        # gcd(1, 4), gcd(3, 4)
        (5, [1, 2, 3, 4]),  # all <5 except 0 coprime to 5
        (6, [1, 5]),        # gcd(1,6)=1, gcd(5,6)=1
        (8, [1, 3, 5, 7]),
        (9, [1, 2, 4, 5, 7, 8]),
        (10, [1, 3, 7, 9]),
        (12, [1, 5, 7, 11])
    ]
)
def test_multiplicative_units(N, expected):
    result = multiplicative_units(N)
    
    assert sorted(result) == sorted(expected)
    assert all(0 <= x < N for x in result)
    assert all(math.gcd(x, N) == 1 for x in result)


def test_unit_clusters_type_and_keys():
    result = unit_clusters(12)
    assert isinstance(result, dict)
    for key in result:
        assert key.startswith("cluster_")
        assert isinstance(result[key], list)
        assert all(isinstance(x, int) for x in result[key])

@pytest.mark.parametrize(
    "N,expected_keys",
    [
        (1, ["cluster_1"]),
        (2, ["cluster_1", "cluster_2"]),
        (4, ["cluster_1", "cluster_2", "cluster_4"]),
        (6, ["cluster_1", "cluster_2", "cluster_3", "cluster_6"]),
    ]
)
def test_unit_clusters_keys(N, expected_keys):
    result = unit_clusters(N)
    assert sorted(result.keys()) == sorted(expected_keys)

@pytest.mark.parametrize(
    "N,expected_cluster_sizes",
    [
        (1, {"cluster_1": 1}),  # units = [0]; (1*0)%1 = 0
        (2, {"cluster_1": 1, "cluster_2": 1}),  # units = [1]
        (3, {"cluster_1": 2, "cluster_3": 1}),  # units = [1,2]
        (4, {"cluster_1": 2, "cluster_2": 1, "cluster_4": 1}),  # units = [1,3]
        (5, {"cluster_1": 4, "cluster_5": 1}),
        (6, {"cluster_1": 2, "cluster_2": 2, "cluster_3": 1, "cluster_6": 1}),
        (7, {"cluster_1": 6, "cluster_7": 1}),
        (8, {"cluster_1": 4, "cluster_2": 2, "cluster_4": 1, "cluster_8": 1}),
        (9, {"cluster_1": 6, "cluster_3": 2, "cluster_9": 1}),
        (10, {"cluster_1": 4, "cluster_2": 4, "cluster_5": 1, "cluster_10": 1}),
        (11, {"cluster_1": 10, "cluster_11": 1}),
        (12, {"cluster_1": 4, "cluster_2": 2, "cluster_4": 2, "cluster_3": 2, "cluster_6": 1, "cluster_12": 1}),
    ]
)
def test_unit_clusters_values(N, expected_cluster_sizes):
    result = unit_clusters(N)
    for key, expected_len in expected_cluster_sizes.items():
        assert len(result[key]) == expected_len
