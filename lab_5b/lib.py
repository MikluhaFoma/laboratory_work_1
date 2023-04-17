from collections import defaultdict
# Алгоритм Тарьяна
class Graph:
    def __init__(self):
        self.nodes = set() # множество узлов
        self.edges = {} # множество рёбер

    def add_node(self, value): # метод добавления вершины
            self.nodes.add(value) # добавляем вершину в множество узлов
            if value not in self.edges:
                self.edges[value] = [] # создаём список рёбер для вершины

    def add_edge(self, start, end): # метод добавления ребра между вершинами
            self.edges[start].append(end)

    def topological_sort(self): # метод топологической сортировки графа
            visited = set() # переменная для отслеживания посещённых вершин
            stack = [] # переменная для ещё не посещённых вершин
            result = [] # переменная для сохранения отсортированных вершин

            def dfs(node): # обходим рекурсивно граф в глубину для посещения всех вершин
                visited.add(node)
                for neighbor in self.edges[node]: # проверяем были ли посещены соседние вершины
                    if neighbor not in visited: # если не посещены, посещаем
                        dfs(neighbor)
                stack.append(node)
            for node in self.nodes:
                if node not in visited:
                    dfs(node)
            while stack:
                result.append(stack.pop()) # добавляем все вершины
            return result

class node:
    def __init__(self):
        self.ErgodicClass = []
