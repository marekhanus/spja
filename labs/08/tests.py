import tempfile

from tasks import parse_graph, shortest_path, bonus_shortest_path_weighted


def test_parse_graph():
    tmp = tempfile.NamedTemporaryFile()

    with open(tmp.name, "w") as f:
        f.write("""4
        0-1
        0-2
        2-1
        2-3
        3-2
""")

    try:
        assert parse_graph(tmp.name) == [[1, 2], [], [1, 3], [2]]
    finally:
        tmp.close()


def test_shortest_path():
    graph_a = [[1], [2], [4], [1], [3, 5], []]

    assert shortest_path(graph_a, 3, 2) == [3, 1, 2]
    assert shortest_path(graph_a, 0, 5) == [0, 1, 2, 4, 5]
    assert shortest_path(graph_a, 5, 2) is None

    graph_b = [[1], [2, 3, 4], [], [4, 5], [], [2]]

    assert shortest_path(graph_b, 0, 3) == [0, 1, 3]
    assert shortest_path(graph_b, 5, 0) is None
    assert shortest_path(graph_b, 1, 2) == [1, 2]
    assert shortest_path(graph_b, 1, 1) == [1]


def test_bonus_shortest_path_weighted():
    graph = [[(1, 20), (2, 10)], [(3, 33), (4, 20)], [(3, 10), (4, 50)],
             [(5, 1)], [(3, 20), (5, 2)], []]

    assert bonus_shortest_path_weighted(graph, 0, 5) == 21
    assert bonus_shortest_path_weighted(graph, 0, 3) == 20
    assert bonus_shortest_path_weighted(graph, 4, 2) is None
