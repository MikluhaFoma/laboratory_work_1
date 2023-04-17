from lib import *

hash_table = HashMap() # Создание экземпляра хэш-таблицы

#Добавление элементов
hash_table.set('apple', 10)
hash_table.set('banana', 20)
hash_table.set('cherry', 30)

#Получение значений элементов
print(hash_table.get('apple'))
print(hash_table.get('banana'))
print(hash_table.get('cherry'))

hash_table.delete('banana') # Удаление элемента

print(hash_table.get('banana')) # Проверка удаления элемента
