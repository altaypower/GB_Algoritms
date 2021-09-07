"""
Написать программу, которая обходит не взвешенный
ориентированный граф без петель, в котором все вершины
связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции,
которая принимает на вход число вершин.
"""

def grapth_generate(n):
    my_list = [[[None]], [[1], [None]], [[1], [2], [1]], [[1, 3], [2], [1], [1]],\
               [[1, 3, 4], [2], [1], [1], [2]], [[1, 3, 4], [2, 5], [1], [1, 5], [2], [None]],\
               [[1, 3, 4], [2, 5], [1, 6], [1, 5], [2, 6], [6], [5]],\
               [[1, 3, 4], [2, 5], [1, 6], [1, 5, 7], [2, 6], [6], [5], [6]]]

    if 1 < n < 9:
        return my_list[n-1]
    else:
        print(f"Узлов не более 8")



def dfs(g):
    start = 0
    n = len(g)
    stop = n - 1
    is_visited = [False] * n
    is_visited[0] = True

    def recurs(start):
        is_visited[start] = True
        if start == stop:
            return f"Путь существует"
        elif start != stop:
            _ = -1
            while _ < len(g[start]) - 1:
                _ +=1
                if not is_visited[g[start][_]]:
                    start = g[start][_]
                    return recurs(start)
            i = -1
            while i < n - 1:
                i += 1
                if start in g[i] and is_visited[i]:
                    start = i
                    return recurs(start)
            return f"Пути нет"

    return recurs(start)

n = int(input("Сколько узлов должно быть в графе: "))
assert 0 < n < 9, "Узлов не более 8"
g = grapth_generate(n)
if g != None:
    print(dfs(g))

