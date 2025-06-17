"""
Unit tests for tonnetz visualization export functions in visualizers.py
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch, PropertyMock

import pytest

from dissig.tonnetze.visualizers import nx_viz


@pytest.mark.parametrize("mode, expect_clusters", [
    ("dot", True),
    ("neato", False),
])
def test_nx_viz_modes(mode, expect_clusters, tmp_path):
    """Test nx_viz with and without arithmetic clusters depending on mode"""

    tonnetz = MagicMock()
    tonnetz.sample_count = 12
    tonnetz.integer_list = [1, 5, 7]

    # Mock the graph returned by tonnetz.network
    mock_graph = MagicMock()
    mock_graph.nodes = {0: {}, 1: {}, 2: {}}
    mock_graph.edges.return_value = [(0, 1, {"weight": 1}), (1, 2, {"weight": 2})]
    tonnetz.network = mock_graph

    # Mocks for external dependencies
    mock_agraph = MagicMock()
    mock_clusters = {"cluster1": [0, 1], "cluster2": [2]}

    with patch("dissig.tonnetze.visualizers.to_agraph", return_value=mock_agraph), \
         patch("dissig.tonnetze.visualizers.unit_clusters", return_value=mock_clusters) as patch_clusters, \
         patch("dissig.tonnetze.visualizers.Path") as mock_path_cls:

        # Fake path resolution
        mock_resolved = MagicMock(spec=Path)
        mock_src = MagicMock(spec=Path)
        type(mock_resolved).name = PropertyMock(
            side_effect=["visualizers.py", "tonnetze", "dissig", "src"]
        )
        type(mock_resolved).parent = PropertyMock(
            side_effect=[MagicMock(), MagicMock(), mock_src, tmp_path]
        )

        mock_path_cls.return_value = MagicMock(resolve=MagicMock(return_value=mock_resolved))

        nx_viz(tonnetz, "my_test_graph", mode=mode)

        assert mock_agraph.layout.called
        assert mock_agraph.draw.call_count >= 1

        if expect_clusters:
            patch_clusters.assert_called_once_with(12)
        else:
            patch_clusters.assert_not_called()
