"""
Build the tone network (tonnetz) for signals of a given modulus, i.e., a given sample count.
"""
from __future__ import annotations

import networkx as nx

class Tonnetz():    
    """
    A tonnetz (tone network) for discrete signals, represented as a weighted directed graph.

    This class constructs a graph of `sample_count` vertices where each vertex represents
    a pitch class or other discrete unit. Edges are created using a provided list of integer
    multipliers that define intervallic relationships. The graph is weighted and directed,
    with weights corresponding to the applied multipliers.

    Attributes:
        sample_count (int): Number of vertices in the network, typically representing
            discrete pitch classes or tonal units.
        integer_list (list[int]): List of integer multipliers used to generate edges between vertices.
        network (nx.DiGraph): A NetworkX directed graph representing the Tonnetz.
    """
    def __init__(self, sample_count : int, integer_list : list[int], include_loops : bool=False, include_zero : bool=False):
        assert isinstance(sample_count, int)
        assert sample_count >= 1
        assert isinstance(integer_list, list)
        assert all([isinstance(entry, int) for entry in integer_list])
        assert isinstance(include_loops, bool)
        assert isinstance(include_zero, bool)

        self.sample_count = sample_count
        self.integer_list = integer_list

        self.include_loops = include_loops
        self.include_zero = include_zero

        self.network = self.generate_network(self.integer_list)

    def generate_weighted_edges(self, new_integer_list : list[int]) -> list[tuple[int, int, int]]:
        """
        Generate a list of weighted directed edges based on a list of integer multipliers.

        Each vertex in the graph is connected to other vertices determined by multiplying
        its index with each value in `new_integer_list` (modulo `self.sample_count`). The
        weight of each edge is the corresponding multiplier.

        Args:
            new_integer_list (list[int]): A list of integer multipliers used to compute edges.

        Returns:
            list[tuple[int, int, int]]: A list of triples (source, target, weight) representing
            the weighted edges of a directed graph.
        """
        assert isinstance(new_integer_list, list)
        assert all([isinstance(entry, int) for entry in new_integer_list])
        
        vertices = range(self.sample_count)
        new_weighted_edges = []
        for source_vertex in vertices:
            for interval_multiplier in new_integer_list:
                target_vertex = (source_vertex * interval_multiplier) % self.sample_count
                current_edge = (source_vertex, target_vertex, interval_multiplier)

                if not self.include_loops and source_vertex == target_vertex:
                    continue

                new_weighted_edges.append(current_edge)
            
        return new_weighted_edges

    def generate_network(self, new_integer_list: list[int]) -> nx.DiGraph:
        """
        Generate a directed graph where all vertices from 0 to sample_count - 1 are included,
        even if they are not connected by any edges.
        """
        if self.include_zero:
            vertices = range(self.sample_count)
        else:
            vertices = range(1, self.sample_count)

        weighted_edges = self.generate_weighted_edges(new_integer_list)
        
        new_network = nx.DiGraph()
        new_network.add_nodes_from(vertices)
        new_network.add_weighted_edges_from(weighted_edges)

        return new_network
