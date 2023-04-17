from lib import *
# Объединение циклов.
def FindEulerPath(orig, i, answer): # Функция нахождения Эйлерова цикла в графе
    for j in range(len(orig[0])): # Проходимся по смежным с данной вершинам
        if orig[i][j] != 0: # Удаляем рёбра, чтобы не возвращаться к данным вершинам
            orig[i][j] = 0
            answer = FindEulerPath(orig, j, answer) # Рекурсивно находим все вершины графа
    answer.append(i)
    return answer # Возвращаем список вершин

def CyclesUnion(orig, start): # Функция
    answer = []
    checkVertical = [0] * len(orig[0]) # Переменная для хранения входящих рёбер
    checkHorizontal = [0] * len(orig[0]) # Переменная для хранения выходящих рёбер
    for i in range(len(orig[0])): # Проходимся по всем вершинам графа
        for j in range(len(orig[0])):
            if orig[i][j] != 0:
                checkHorizontal[i] += 1
                checkVertical[j] += 1
    for i in range(len(orig[0])):
        if checkVertical[i] != checkHorizontal[i] and checkHorizontal[i] != 0 and checkVertical[i] != 0: # Проверка равенства количества входящих и выходящих рёбер
            return None # Если нет циклов
    answer = FindEulerPath(orig, start, answer) # Вызываем функцию поиска эйлерова цикла
    return answer
# --------------------------------------------------------------------
# Алгоритм Флёри.
def Fleury(orig, start):
    answer = []
    checkVertical = [0] * len(orig[0]) # Переменная для хранения рёбер, инцидентных каждой вертикали графа
    checkHorizontal = [0] * len(orig[0]) # Переменная для хранения рёбер, инцидентных каждой горизонтали графа
    findBridge = [0] * len(orig[0]) # Количество мостов, инцидентных каждой вертикали графа
    count = 0 # количество ребер в графе

    for i in range(len(orig[0])): # Проходимся по всем вершинам графа
        for j in range(len(orig[0])):
            if orig[i][j] != 0:
                count += 1
                checkHorizontal[i] += 1 # Подсчитываем количество ребер, инцидентных каждой вертикали
                checkVertical[j] += 1 # Подсчитываем количество ребер, инцидентных каждой горизонтали
                findBridge[j] += 1 # Подсчитываем количество мостов, инцидентных каждой вертикали

    for i in range(len(orig[0])): # Проверяем возможность построения Эйлерова цикла путем сравнения количества ребер, инцидентных каждой вертикали и горизонтали
        if checkVertical[i] != checkHorizontal[i] and checkHorizontal[i] != 0 and checkVertical[i] != 0:
            return None

    while count > 0: # Опять проходимся по всем вершинам
        for i in range(start, len(orig[0])):
            if orig[start][i] != 0 and findBridge[i] > 1: # Если мост соединяющий вершины не единственный, то удаляем один из мостов
                orig[start][i] = 0
                answer.append(Node(start, i)) # Добавляем мост в ответ
                start = i
                checkHorizontal[start] -= 1
                count -= 1
                break
            elif orig[start][i] != 0 and checkHorizontal[start] == 1: # Если мост единственный, добавляем его в ответ и удаляем.
                orig[start][i] = 0
                answer.append(Node(start, i))
                start = i
                checkHorizontal[start] -= 1
                count -= 1
                break
    return answer
# -----------------------------------------------------------------------
# Алгоритм Косайрио
def kosaraju(orig):
    answer = [] # Создаём список для записи ответа

    # транспонирование графа
    for i in range(orig[0].__len__() - 1):
        for j in range(i + 1, orig[0].__len__()):
            tmp = orig[i][j]
            orig[i][j] = orig[j][i]
            orig[j][i] = tmp

    visited = [False] * orig[0].__len__() # Переменная для хранения посещённых вершин
    stack = [-5] # Переменная для вершин графа, добавляемые в порядке их завершения обхода в глубину
    for i in range(visited.__len__()):
        if not visited[i]:
            dfs_inv(orig, i, visited, stack) # Обходим граф в глубину
    visited = [False] * orig[0].__len__() # Список вершин, которые были посещены при обходе графа в глубину
    while stack[-1] != -5:
        tmp = stack.pop()
        if not visited[tmp]:
            component = dfs(orig, tmp, visited, node()) # Выполняем обход графа в глубину для вершин, которые не были посещены
            answer.append(component.ErgodicClass)

    stack.pop()
    return answer


def dfs_inv(orig, peak, visited, stack): # Обход в глубину транспонированного графа
    visited[peak] = True
    for j in range(0, orig[0].__len__()):
        if orig[peak][j] != 0 and not visited[j]:
            dfs_inv(orig, j, visited, stack)
    stack.append(peak)

def dfs(orig, peak, visited, part_of_answer): # Обход оригинального графа
    visited[peak] = True
    part_of_answer.ErgodicClass.append(peak)
    for i in range(visited.__len__()):
        if not visited[i] and orig[i][peak] != 0:
            part_of_answer = dfs(orig, i, visited, part_of_answer)
    return part_of_answer

if __name__ == "__main__":
    print("Алгоритм Тарьяна: ")
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(2, 0)
    print("Результат:", g.topological_sort())

    print("\nАлгоритм Флйри: ")
    graph = [[0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0]]
    print("Граф:", graph)
    euler_path = CyclesUnion(graph, 0)
    print("Результат:", euler_path)

    print("\nАлгоритм Объединения циклов: ")
    RightA = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0]]
    print("Граф:", graph)
    print("Результат:", CyclesUnion(RightA, 0))

    print("\nАлгоритм Косайрио: ")
    graph = [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0]]
    print("Граф:", graph)
    answer = kosaraju(graph)
    print("Результат:", answer)
