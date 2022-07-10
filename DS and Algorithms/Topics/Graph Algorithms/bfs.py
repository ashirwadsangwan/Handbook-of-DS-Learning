graph = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def BFSIterative(graph, sourceNode):
    queue = [sourceNode]

    while len(queue) > 0:
        current = queue[0]
        del queue[0]
        print(current)

        for neighbour in graph[current]:
            queue.append(neighbour)


if __name__ == "__main__":

    print(BFSIterative(graph, "a"))
