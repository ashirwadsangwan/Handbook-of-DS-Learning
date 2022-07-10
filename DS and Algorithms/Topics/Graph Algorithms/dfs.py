graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def depthFirstPrint(graph, sourceNode):
    ## we'll use a stack
    stack = [sourceNode]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)


def DFSRecursion(graph, sourceNode):
    print(sourceNode)
    for neighbour in graph[sourceNode]:
        DFSRecursion(graph, neighbour)


if __name__ == "__main__":

    print(DFSRecursion(graph, "a"))
