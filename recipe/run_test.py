import pytest
from streamlit_agraph import agraph, Node, Edge, Config


def test_can_create_objects():
    # just check that we can instantiate without errors
    Node(id="A", label="Alpha")
    Edge(source="A", target="B", label="connects")
    Config(width=400, height=300, directed=True)


def test_agraph_does_not_crash():
    nodes = [Node(id="1"), Node(id="2")]
    edges = [Edge(source="1", target="2")]
    config = Config(width=200, height=200, directed=True, physics=False)

    # smoke test: should not raise any exception
    try:
        agraph(nodes=nodes, edges=edges, config=config)
    except Exception as e:
        pytest.fail(f"agraph raised an exception: {e}")