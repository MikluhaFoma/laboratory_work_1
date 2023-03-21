class Graph: # для Крускала
    def __init__(self, vertex):
        self.V = vertex #количество вершин
        self.graph = [] #граф

    def add_edge(self, u, v, w): #Добавляем ребро с весом w между вершинами u v
        self.graph.append([u, v, w])

    def search(self, parent, i):#Нахождение корневой вершины
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):#объединение деревьев
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2]) #сортируем рёбра в порядке возрастания весов
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1: #проверка на цикл
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])#записываем в результат
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",u, v,end =" ")
            print("-",weight)

class GraphB:#для Прима
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.vertices[vertex1].append((vertex2, weight))
        self.vertices[vertex2].append((vertex1, weight))
