# Based on https://github.com/ChrisDelClea/streamlit-agraph/blob/master/README.md?plain=1#L12-L47
import pytest
from streamlit_agraph import Node, Edge, Config, agraph

@pytest.fixture
def sample_graph():
    nodes = [
        Node(
            id="Spiderman",
            label="Peter Parker",
            size=25,
            shape="circularImage",
            image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png"
        ),
        Node(
            id="Captain_Marvel",
            size=25,
            shape="circularImage",
            image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"
        )
    ]
    edges = [
        Edge(
            source="Captain_Marvel",
            label="friend_of",
            target="Spiderman"
        )
    ]
    config = Config(
        width=750,
        height=950
    )
    return nodes, edges, config


def test_graph_structure(sample_graph):
    nodes, edges, config = sample_graph

    # --- Nodes ---
    assert any(node.id == "Spiderman" for node in nodes)
    assert any(node.id == "Captain_Marvel" for node in nodes)

    # --- Edges ---
    edge = edges[0]
    assert edge.to == "Spiderman"
    assert getattr(edge, "from") == "Captain_Marvel"

    # --- Config ---
    cfg = config.to_dict()
    assert cfg["width"] == "750px"
    assert cfg["height"] == "950px"

def test_agraph_runs(sample_graph):
    nodes, edges, config = sample_graph
    try:
        agraph(nodes=nodes, edges=edges, config=config)
    except Exception as e:
        pytest.fail(f"agraph threw an exception: {e}")