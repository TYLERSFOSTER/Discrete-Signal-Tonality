import pytest
import networkx as nx

from dissig.tonnetze.network import Tonnetz


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
    t = Tonnetz(sample_count, [], include_loops=include_loops)
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
