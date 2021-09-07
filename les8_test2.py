"""
Доработать алгоритм Дейкстры,
чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijcstra(grapth, start):
    length = len(grapth)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    root = start
    path = {}
    for _ in range(length):
        path[_] = []
    print(path)

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(grapth[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i in range(length):
        if cost[i] == float('inf'):
            path[i].append('нет пути')
        elif parent[i] == -1:
            path[i].append(i)
        else:
            j = i
            path[i].append(i)
            while parent[j] != root:
                path[i].append(parent[j])
                j = parent[j]
            path[i].append(root)
    for i in range(length):
        path[i].reverse()
        print(f"Путь к вершине {i}: {path[i]}, а стоимость: {cost[i]}")

s = int(input("От какой вершины идти: "))
dijcstra(g, s)
