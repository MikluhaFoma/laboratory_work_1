#!/usr/bin/env python
class PriorityQueue:
    def __init__(self):
        self.mas = []
        self.size = 0

    def show(self):#Вывод
        for i in range(self.size):
            print(self.mas[i])

    def void_mas(self):#Проверка на пустоту
        if len(self.mas) == 0:
            print("queue is clear")
        else:
            self.show()

    def len_queue(self):#Вычисление длины
        print(self.size)

    def addElement(self, item):#Добавление элементов
        self.size += 1
        self.mas.append(item)
        i = self.size - 1
        parent = (i - 1) // 2

        while ((i > 0) and self.mas[parent] < self.mas[i]):
            temp = self.mas[i]
            self.mas[i] = self.mas[parent]
            self.mas[parent] = temp

            i = parent
            parent = (i - 1) // 2

    def del_element(self, index):#Удаление элемента
        self.mas[index] = -1
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            large = index

            if left < self.size and self.mas[left] > self.mas[large]:
                large = left

            if right < self.size and self.mas[right] > self.mas[large]:
                large = right

            if large == index:
                break

            temp = self.mas[index]
            self.mas[index] = self.mas[large]
            self.mas[large] = temp
            index = large
        self.mas.pop(index)
        self.size -= 1

    def print_max_element(self):#Вывод максимального элемента
        print(self.mas[0])
        
if __name__ == "__main__":
    q = PriorityQueue()
    q.void_mas()
    q.addElement(1)
    q.addElement(6)
    q.addElement(3)
    q.addElement(5)
    q.addElement(9)
    q.addElement(8)
    q.addElement(7)
    q.addElement(11)
    q.addElement(15)
    q.void_mas()
    print()
    print("Количество элементов очереди:")
    q.len_queue()
    print()
    print("Максимальный элемент очереди:")
    q.print_max_element()
    print()
    q.del_element(0)
    print("После удаления максимального элемента:")
    q.show()
