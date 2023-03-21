#!/usr/bin/env python

from lib import*
from collections import deque
import heapq

def DFS(graph, first, visited=None):#поиск в глубину
    if visited is None:#запись вершин, в которых уже побывали
        visited = set()
    visited.add(first)

    print(first)

    for next_item in graph[first] - visited:#обход графа
        DFS(graph, next_item, visited)
    return visited


def BFS(graph, start_vertex):#обход в ширину
    visited = []#создаём список вершин, которые мы посетили и обработали
    queue = deque([start_vertex])# очередь, содержащая вершины, которые мы еще не обработали
    while queue:
        vertex = queue.popleft()# извлекаем вершину из начала очереди
        if vertex not in visited:# если мы еще не обработали эту вершину, то добавляем ее в список visited
            visited.append(vertex)
            # добавляем все смежные вершины в очередь, кроме тех, которые мы уже посетили
            for neighbor in range(len(graph[vertex])):
                    if graph[vertex][neighbor] == 1 and neighbor not in visited:
                            queue.append(neighbor)
    return visited

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}#сохраняем дистанции от первой вершины до остальных
    distances[start] = 0
    pq = [(0, start)]#расстояние до вершины, вершина
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)#достаём наименьшее расстояние и вершину
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():#вычисляем новое расстояние
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances#возвращаем кратчайшие расстояние от начальной вершины до остальных


def prim_algorithm(graph, start_vertex):
    visited = set([start_vertex])#посещённые вершины
    edges = []#минимальные рёбра
    min_edge = (None, None, float('inf'))#связь посещённой и не посещённой вершины
    while len(visited) != len(graph.vertices):#проходим все вершины
        for vertex in visited:#перебор вершин и связывающие их ребра
            for neighbor, weight in graph.vertices[vertex]:
                if neighbor not in visited:#если вес текущего ребра меньше текущего меньшего между посещённой и не посещённой врершиной
                    if weight < min_edge[2]:#если меньше, то заменяем
                        min_edge = (vertex, neighbor, weight)
        edges.append(min_edge)
        visited.add(min_edge[1])
        min_edge = (None, None, float('inf'))#сброс для поиска нового минимального ребра

    return edges


def floyd_warshall_algorithm(graph):
    n = len(graph)#размер графа
    dist = graph
    for k in range(n):#выполняется раз равное количеству вершин
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])#обновляются значения мингимального расстояния между вершинами

    return dist#матрица с кротчайшими расстояниями между парами вершин графа

if __name__ == "__main__":
    # Поиск в глубину
    graph = {'0': set(['1', '3']),
             '1': set(['0', '2']),
             '2': set(['0', '1', '4']),
             '3': set(['0']),
             '4': set(['2'])}
    print("Поиск в глубину\n граф:", graph)
    print("Результат:")
    DFS(graph, '0')

    # Поиск в ширину
    graph = [[0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]]
    print("\nПоиск в ширину\n граф:", graph)
    print("Результат:")
    print(BFS(graph, 0))

    # Алгоритм Курскала
    print("\nАлгоритм Курскала\n")
    g = Graph(5)
    g.add_edge(0, 1, 8)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, 9)
    g.add_edge(1, 3, 11)
    g.add_edge(2, 3, 15)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 7)
    print("Результат:")
    g.kruskal()
    # Алгоритм Дейкстры
    graph = {'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}}
    print("\nАлгоритм Дейкстры\n граф:", graph)
    print("Результат:")
    print(dijkstra(graph, 'A'))

    # Алгоритм Прима
    g = GraphB()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 1)
    g.add_edge('B', 'E', 4)
    g.add_edge('C', 'E', 2)
    g.add_edge('D', 'E', 3)
    print("\nАлгоритм Прима\n граф:", graph)
    print(g.vertices)
    print("Результат:")
    edges = prim_algorithm(g, 'B')
    for edge in edges:
        print(edge)

    # Алгоритм Флойда-Уоршала
    graph = [[0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]]
    print("\nАлгоритм Флойда-Уоршала\n граф:", graph)
    distances = floyd_warshall_algorithm(graph)
    print("Результат:")
    for i in range(len(distances)):
        for j in range(len(distances[i])):
            print(distances[i][j], end='\t')
        print()
