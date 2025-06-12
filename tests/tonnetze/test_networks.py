from __future__ import annotations

from unittest.mock import MagicMock

import pytest
import networkx as nx

from dissig.tonnetze.networks import Tonnetz, SignalTonnetz


@pytest.mark.parametrize(
    "sample_count, integer_list, include_loops, expected_edges",
    [
        # Basic case: no loops
        (5, [2], False, [(1, 2, 2), (2, 4, 2), (3, 1, 2), (4, 3, 2)]),
        # Loops included
        (5, [1], True, [(0, 0, 1), (1, 1, 1), (2, 2, 1), (3, 3, 1), (4, 4, 1)]),
        # Multiple multipliers
        (3, [1, 2], False, [(1, 2, 2), (2, 1, 2)]),
    ]
)
def test_generate_weighted_edges(sample_count, integer_list, include_loops, expected_edges):
    t = Tonnetz(sample_count, [], include_loops=include_loops, include_zero=True)
    result = t.generate_weighted_edges(integer_list)
    # Sort for comparison
    assert sorted(result) == sorted(expected_edges)


@pytest.mark.parametrize(
    "sample_count, integer_list, include_loops, include_zero, expected_nodes, expected_edge_count",
    [
        # include_zero=False, excludes node 0
        (4, [3], False, False, [1, 2, 3], 2),
        # include_zero=True, includes node 0
        (4, [3], False, True, [0, 1, 2, 3], 2),
        # include_loops suppresses self-edges
        (5, [1], False, True, [0, 1, 2, 3, 4], 0),
        # loops allowed
        (5, [1], True, True, [0, 1, 2, 3, 4], 5),
    ]
)
def test_generate_network(sample_count, integer_list, include_loops, include_zero, expected_nodes, expected_edge_count):
    t = Tonnetz(sample_count, integer_list, include_loops=include_loops, include_zero=include_zero)
    G = t.network
    assert set(G.nodes) == set(expected_nodes)
    assert isinstance(G, nx.DiGraph)
    assert G.number_of_edges() == expected_edge_count


@pytest.fixture
def mock_signal():
    signal = MagicMock()
    signal.__len__.return_value = 4
    signal.scale_time_by.side_effect = lambda x: f"signal_scaled_by_{x}"
    return signal

@pytest.mark.parametrize(
    "integer_list, expected_edges",
    [
        ([1], [(1, 1, 1), (2, 2, 1), (3, 3, 1)]),             # self loops
        ([2], [(1, 2, 2), (2, 0, 2), (3, 2, 2)]),
        ([1, 3], [(1, 1, 1), (1, 3, 3), (2, 2, 3), (3, 3, 1), (3, 1, 3)]),
    ]
)
def test_SignalTonnetz_edge_construction(mock_signal, integer_list, expected_edges):
    tonnetz = SignalTonnetz(mock_signal, integer_list, include_loops=True, include_zero=False)
    edges = list(tonnetz.network.edges(data="weight")) # type: ignore
    edges_as_tuples = [(u, v, w) for u, v, w in edges]
    assert sorted(edges_as_tuples) == sorted(expected_edges)


@pytest.mark.parametrize("include_zero", [True, False])
def test_SignalTonnetz_include_zero_node(mock_signal, include_zero):
    tonnetz = SignalTonnetz(mock_signal, [1], include_zero=include_zero)
    expected_nodes = list(range(4)) if include_zero else list(range(1, 4))
    assert sorted(tonnetz.network.nodes) == expected_nodes


@pytest.mark.parametrize("include_loops", [True, False])
def test_SignalTonnetz_include_loops_behavior(mock_signal, include_loops):
    tonnetz = SignalTonnetz(mock_signal, [1], include_loops=include_loops, include_zero=False)
    for u, v in tonnetz.network.edges():
        if not include_loops:
            assert u != v


@pytest.mark.parametrize(
    "vertex, expected_key",
    [(1, "signal_scaled_by_1"), (2, "signal_scaled_by_2"), (3, "signal_scaled_by_3")]
)
def test_SignalTonnetz_propagated_signals(mock_signal, vertex, expected_key):
    tonnetz = SignalTonnetz(mock_signal, [1], include_loops=True, include_zero=False)
    node_data = tonnetz.network.nodes[vertex]
    assert "signal" in node_data
    assert node_data["signal"] == expected_key


@pytest.mark.parametrize(
    "tonic_len, should_raise",
    [(0, True), (1, False), (5, False)]
)
def test_SignalTonnetz_signal_length_validation(tonic_len, should_raise):
    signal = MagicMock()
    signal.__len__.return_value = tonic_len
    signal.scale_time_by.return_value = "stub"

    if should_raise:
        with pytest.raises(AssertionError):
            SignalTonnetz(signal, [1])
    else:
        tonnetz = SignalTonnetz(signal, [1])
        assert isinstance(tonnetz.network, nx.DiGraph)