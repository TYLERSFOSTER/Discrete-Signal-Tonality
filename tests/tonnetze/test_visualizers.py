import pytest
from unittest.mock import MagicMock, patch
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
         patch("dissig.tonnetze.visualizers.Path") as patch_path:

        # --- Patch Path resolution to avoid actual disk writing ---
        mock_path_obj = MagicMock(spec=Path)
        patch_path.return_value = mock_path_obj
        mock_path_obj.resolve.return_value.parents.__getitem__.return_value = tmp_path

        # --- Run function ---
        nx_viz(tonnetz, "my_test_graph", arithmetic_clusters=arithmetic_clusters)

        # --- Check image was rendered and saved ---
        assert mock_agraph.layout.called
        assert mock_agraph.draw.call_count >= 1  # At least one draw (maybe two)

        # --- Check clustering was called or not ---
        if expected_cluster_called:
            patch_clusters.assert_called_once_with(12)
        else:
            patch_clusters.assert_not_called()
