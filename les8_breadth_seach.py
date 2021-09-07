"""
Поиск кратчайшего пути в ширину
"""

from collections import deque

# Используется такая матрица графа
g=[
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

def bfs(grapth, start, finish):
    parent = [None for _ in range(len(grapth))]
    is_visited = [False for _ in range(len(grapth))]

    deq = deque([start])
    is_visited[start] = True
    while len(deq) > 0:
        curent = deq.pop()
        if curent == finish:
            break

        for i, vertex in enumerate(grapth[curent]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)

    else:
        return f"Из вершины {start} нельзя попасть в вершину {finish}"

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f"Кратчайший путь {list(way)} длиною в {cost}"


s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(bfs(g, s, f))