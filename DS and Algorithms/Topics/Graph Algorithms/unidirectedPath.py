edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]


def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    return graph


def searchPath(graph, source, dest):
    """Find if a path exists between source and destination

    Args:
        source (str): source node
        dest (str): destination node
    Return: Bool
    """
    flag = False
    visited = [source]
    traversed = set()
    while len(visited) > 0:
        current = visited.pop()
        traversed.add(current)
        if current == dest:
            flag = True
        for neighbour in graph[current]:
            if neighbour not in traversed:
                visited.append(neighbour)
            else:
                pass

    return flag


def undirected_path(edges, node_A, node_B):
    """Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
    The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

    Args:
        edges (list): list of nodes
        node_A (str): node
        node_B (str): node
    """
    graph = buildGraph(edges)
    return searchPath(graph, node_A, node_B)


if __name__ == "__main__":
    print(undirected_path(edges, "i", "l"))
