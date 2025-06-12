from __future__ import annotations

import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from pathlib import Path

from dissig.tonnetze.visualizers import nx_viz


@pytest.mark.parametrize("arithmetic_clusters, expected_cluster_called", [
    (True, True),
    (False, False),
])
def test_nx_viz(arithmetic_clusters, expected_cluster_called, tmp_path):
    # --- Mock Tonnetz object ---
    tonnetz = MagicMock()
    tonnetz.sample_count = 12
    tonnetz.integer_list = [1, 5, 7]
    
    # --- Mock NetworkX graph structure ---
    mock_graph = MagicMock()
    mock_graph.nodes = {0: {}, 1: {}, 2: {}}
    mock_graph.edges.return_value = [(0, 1, {"weight": 1}), (1, 2, {"weight": 2})]
    tonnetz.network = mock_graph

    # --- Patch to_agraph and unit_clusters ---
    mock_agraph = MagicMock()
    mock_unit_clusters = {"cluster1": [0, 1], "cluster2": [2]}

    with patch("dissig.tonnetze.visualizers.to_agraph", return_value=mock_agraph) as patch_agraph, \
        patch("dissig.tonnetze.visualizers.unit_clusters", return_value=mock_unit_clusters) as patch_clusters, \
        patch("dissig.tonnetze.visualizers.Path") as mock_path_cls:

        # Set up fake Path resolution tree
        mock_resolved = MagicMock(spec=Path)
        mock_src = MagicMock(spec=Path)
        mock_project_root = tmp_path

        type(mock_resolved).name = PropertyMock(side_effect=["visualizers.py", "tonnetze", "dissig", "src"])
        type(mock_resolved).parent = PropertyMock(side_effect=[MagicMock(), MagicMock(), mock_src, mock_project_root])

        mock_path_cls.return_value = MagicMock(resolve=MagicMock(return_value=mock_resolved))

        nx_viz(tonnetz, "my_test_graph", arithmetic_clusters=arithmetic_clusters)

        assert mock_agraph.layout.called
        assert mock_agraph.draw.call_count >= 1

        if expected_cluster_called:
            patch_clusters.assert_called_once_with(12)
        else:
            patch_clusters.assert_not_called()

