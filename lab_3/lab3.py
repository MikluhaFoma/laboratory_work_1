class BTreeNode: #Класс для узла
    def __init__(self, N, leaf):
        self.N = N #количество ключей
        self.leaf = leaf #для проверки на лист (крайний элемент в дереве)
        self.keys = [] #ключи
        self.values = [] #знаения
        self.children = [] #ссылки на потомков

class BTreeMap: #Класс для ассациативного массива
    def __init__(self, N):
        self.N = N #кол-во ключей в каждом узле
        self.root = None #корень дерева

    def get(self, key):# получение знаения по ключу
        if self.root is None: # если ключ не связан с значением
            return None
        else:
            return self.Get(key, self.root) #возвращаем найденное значенине

    def Get(self, key, node):# метод поиска значения по ключу
        i = 0
        while i < len(node.keys) and key > node.keys[i]: # пока есть ключ и искомый ключ не больше чем требуется
            i += 1
        if i < len(node.keys) and key == node.keys[i]: # если искомый ключ найден, возвращаем соответсвующее значение
            return node.values[i]
        elif node.leaf: # если ключ является листом, возвращаем None
            return None
        else:
            return self.Gget(key, node.children[i]) # если ключ не найден в данном узле, ищем его в следующем

    def set(self, key, value): # метод добавление элемента в дерево
        if self.root is None: # если элементов ещё нет
            self.root = BTreeNode(self.N, True) # создаём новый объект, назначая его листом
            self.root.keys.append(key) # добавляем ключь
            self.root.values.append(value) # добавляем значение
        else:
            node = self.root # присваеваем узлу корень
            if len(node.keys) == 2 * self.N - 1: # если узел не лист
                new_root = BTreeNode(self.N, False) # создаёмновый дочерний узел
                new_root.children.append(node)
                self.Split_child(new_root, 0, node)
                node = new_root
                self.root = new_root
            self.Set(key, value, node)

    def Set(self, key, value, node):
        i = 0
        while i < len(node.keys) and key > node.keys[i]: # пока есть ключ
            i += 1
        if node.leaf: # если узел - лист
            node.keys.insert(i, key) # добавляем значение ключа
            node.values.insert(i, value) # добавляем значение по ключу
        else:
            if len(node.children[i].keys) == 2 * self.N - 1: # если количетсво узлов потомков на один меньше, чем удвоенное значение ключей, добавляем новый узел в глубину
                self.Split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1
            self.Set(key, value, node.children[i])

    def Split_child(self, parent, i, child):
        new_child = BTreeNode(child.N, child.leaf) # дублируем узел
        parent.children.insert(i + 1, new_child) # вставляем новый узел
        parent.keys.insert(i, child.keys[self.N - 1]) # записывем текущий ключ в прошлый узел
        parent.values.insert(i, child.values[self.N - 1]) # записываем текущее значение в прошлый узел
        new_child.keys = child.keys[self.N:] # присваеваем прошлый клчю
        new_child.values = child.values[self.N:] # присваеваем прошлое значение
        child.keys = child.keys[:self.N - 1] # переписываем ключи
        child.values = child.values[:self.N - 1] # переписываем значения
        if not child.leaf: # если узел не лист, помещаем узел в конец
            new_child.children = child.children[self.N:]
            child.children = child.children[:self.N]

    def update(self, key, value):
        node = self.root # присваеваем начало дерева
        while node is not None: # пока дерево не закончено
            i = 0
            while i < len(node.keys) and key > node.keys[i]: # пока есть ключ
                i += 1
            if i < len(node.keys) and key == node.keys[i]: # если ключ найден
                node.values[i] = value # заменяем значение
                return
            if i > self.N: # если текущий ключ больше числа всех, выводим ошибку
                print("Key error. The value has not been overwritten. You can use the key: 0 to", self.N)
                return
            else:
                node = node.children[i] # переходим к следующему узлу
                
if __name__ == "__main__":
    btree_map = BTreeMap(2)
    btree_map.set(1, "one") # добавляем здачение по ключу
    btree_map.set(2, "two")
    btree_map.set(3, "three")
    print(btree_map.get(1)) # выводим результат по ключу
    print(btree_map.get(2))
    print(btree_map.get(3))
    btree_map.update(2, "new two") # изменяем значение по ключу
    print(btree_map.get(2))
