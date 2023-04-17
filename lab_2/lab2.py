class Node: # Класс для узла
    def __init__(self, key, value):
        self.key = key # значение ключа
        self.value = value # значение
        self.left = None # левый потомок
        self.right = None # правый потомок
        self.height = 1 # высота узла (для отслеживания баланса в AVL дереве)

class AVLTree:
    def __init__(self):
        self.root = None # корень дерева

    def get(self, key): # получение значения узла по ключу
        return self.Get(key, self.root)

    def Get(self, key, node):
        if node is None: # если нет узлов, возвращаем None
            return None
        elif key == node.key: # если ключ найден, возврвщаем значение узла
            return node.value
        elif key < node.key: # иначе рекурсивно ищем ключ в левых и правых потомках
            return self.Get(key, node.left)
        else:
            return self.Get(key, node.right)

    def insert(self, key, value): # добавление новой пары ключ-значение
        self.root = self.Insert(key, value, self.root)

    def Insert(self, key, value, node):
        if node is None: # если дерево пусто, создаём новый узел и добавляем туда ключ и значение
            return Node(key, value)
        elif key == node.key: # если такой ключ уже существует, заменяем его значение
            node.value = value
        elif key < node.key: # рекурсивный поиск места для добавление ключа и значения
            node.left = self.Insert(key, value, node.left)
        else:
            node.right = self.Insert(key, value, node.right)

        node.height = 1 + max(self.GetHeight(node.left), self.GetHeight(node.right)) # вычисление нового значения высоты узла
        balance = self.Balance(node) # проверка баланса дерева

        if balance > 1 and key < node.left.key: # если дерево перегружено влево
            return self._rotateRight(node) # выполняем правый поворот

        if balance < -1 and key > node.right.key: # если дерево перегружено вправо
            return self._rotateLeft(node) # делаем левый поворот

        if balance > 1 and key > node.left.key: # если дерево перегружено влево и значение ключа больше значения ключа левого потомка, делаем левый правый поворот
            node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        if balance < -1 and key < node.right.key: # если дерево перегружено вправо и значение ключа больше значения ключа правого потомка, делаем правый левый поворот
            node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)
        return node

    def GetHeight(self, node): # метод вычисления высоты узла
        if node is None: # если узла нет, возвращаем 0
            return 0
        return node.height # иначе возвращаем высоту узла

    def Balance(self, node): # метод для определения баланса узла
        if node is None: # если узла нет, возвращаем 0
            return 0
        return self.GetHeight(node.left) - self.GetHeight(node.right) # иначе вычисляем баланс и возвращаем его

    def _rotateRight(self, node): # реализация правого поворота
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.GetHeight(node.left), self.GetHeight(node.right)) # обновляем высоты узлов
        new_root.height = 1 + max(self.GetHeight(new_root.left), self.GetHeight(new_root.right))
        return new_root

    def _rotateLeft(self, node): # реализация левого поворота
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.GetHeight(node.left), self.GetHeight(node.right)) # обновляем высоты узлов
        new_root.height = 1 + max(self.GetHeight(new_root.left), self.GetHeight(new_root.right))
        return new_root

if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(1, 'one')
    tree.insert(2, 'two')
    tree.insert(4, 'four')
    tree.insert(5, 'five')
    tree.insert(3, 'three')
    print(tree.get(2))  # выводит 'two'
    print(tree.get(3))  # выводит 'three'
    tree.insert(2, 'new two') # замена значения по ключу
    print(tree.get(2))  # выводит 'new two'
    print(tree.get(6))
