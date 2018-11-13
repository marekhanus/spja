def parse_graph(path):
    """
    1 point

    Parse a file located at `path` to a directed graph structure.

    The first line in the file represents the number of vertices in the graph.
    All other lines are in the form X-Y, which represents an edge from vertex
    X to vertex Y. Vertex IDs are zero based so you can use them to index into
    the resulting vertex list.

    The resulting graph should be represented as a list of vertices, where each
    vertex is a list of its neighbour vertices.

    Example:
        graph.txt:
        4
        0-1
        0-2
        2-1
        2-3
        3-2

        parse_graph('graph.txt')
        # [[1, 2], [], [1, 3], [2]]

        Graphical representation of the above graph:
        https://upload.wikimedia.org/wikipedia/commons/5/51/Directed_graph.svg
    """
    pass


def shortest_path(graph, source, destination):
    """
    4 points

    Calculate the shortest path in `graph` from `source` vertex to
    `destination` vertex.

    The input graph is already parsed with the same format as in `parse_graph`,
    `source` and `destination` are zero based vertex indices.

    Return a list of vertices in the shortest path. For 3 points return at least
    the length of the shortest path. If a path between `source` and `destination`
    doesn't exist, return None.

    Hint:
        Use BFS (breadth-first search) with queue.Queue from the standard
        library. The graph is unweighted, so all edges have length 1.

    Example:
          shortest_path([[1], [2], [4], [1], [3, 5], []], 3, 2)
          [3, 1, 2]

          Graphical representation of the above graph:
          https://computersciencewiki.org/index.php/File:Directed_graph.png
    """
    pass


def bonus_shortest_path_weighted(graph, source, destination):
    """
    1 point (bonus)

    Calculate the shortest path in `graph` from `source` vertex to
    `destination` vertex. This time with a weighted graph.

    Graph format is a list of vertices, each vertex is a list of tuples
    (neighbour vertex, distance). Distance is the length of the edge between
    the two vertices.

    Return the shortest distance between `source` and `destination` or None
    if there's no path between them.

    Hint:
        Use Dijkstra's algorithm.
        https://www-m9.ma.tum.de/graph-algorithms/spp-dijkstra/index_en.html

    Example:
          shortest_path([[(1, 20), (2, 10)], [(3, 33), (4, 20)],
          [(3, 10), (4, 50)], [(5, 1)], [(3, 20), (5, 2)], []], 0, 5)
          21

          Graphical representation of the above graph:
          https://computersciencewiki.org/index.php/File:Directed_graph.png
    """
    pass
