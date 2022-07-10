def searchPath(graph, source, dest):
    """Find if a path exists between source and destination

    Args:
        source (str): source node
        dest (str): destination node
    Return: Bool
    """
    flag = False
    visited = [source]

    while len(visited) > 0:
        current = visited.pop()
        if current == dest:
            flag = True
        for neighbour in graph[current]:
            visited.append(neighbour)

    return flag


if __name__ == "__main__":

    graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": [], "k": []}

    print(searchPath(graph, source="f", dest="k"))
