# qianGuang /2019/5/22  /github:CACaptain   /1376420235@qq.com


def BFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)

    parent = {start: None}

    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)

                parent[w] = vertex

        print(vertex)
    return parent

def DFS(graph, start):
    stack = []
    stack.append(start)
    seen = set()
    seen.add(start)
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }

    p = BFS(graph, "E")
    print("---")
    for key in p:
        print(key, p[key])
    print("---")
    v = "B"
    while v is not None:
        print(v)
        v = p[v]
    print("------------")
    print("------------")
    DFS(graph, "A")
