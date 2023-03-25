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
        if rank[xroot] < rank[yroot]:# определяем, какое дерево находится выше (оно будет родителем для другого дерева)
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:# если деревья имеют одинаковую высоту 
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i = 0 # переменная для перебора рёбер
        j = 0 # переменная для подсчёта числа рёбер в минимальном оставном дереве 
        self.graph = sorted(self.graph, key=lambda item: item[2]) #сортируем рёбра в порядке возрастания веса
        parent = [] # список для родителей вершин 
        rank = [] # список для высот деревьев
        for node in range(self.V): # проходимся по всем вершинам графа 
            parent.append(node) # добавляем вершину в списокк родителей 
            rank.append(0)
        while j < self.V - 1: #добавляем рёбра в минимальное оставное дерево
            u, v, w = self.graph[i] # по очереди берем рёбра из списка рёбер
            i = i + 1 # пеерход к следующему ребру 
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y: # проверка на принадлежность вершины одному и тому же дереву
                j = j + 1 # переход к следующему ребру 
                result.append([u, v, w])#записываем в результат
                self.apply_union(parent, rank, x, y) # объединяем деревья 
        for u, v, weight in result:
            print("Рёбра:",u, v, end =" ")
            print("-",weight)

class GraphB:#для Прима
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []# создаём список для хранения рёбер 

    def add_edge(self, vertex1, vertex2, weight):# добавляем рёбра к вершинам 
        self.vertices[vertex1].append((vertex2, weight))
        self.vertices[vertex2].append((vertex1, weight))
