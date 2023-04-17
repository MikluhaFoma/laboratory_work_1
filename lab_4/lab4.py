from lib import *

my_map = hash_map()
# Добавление пары ключ-значение
my_map.set('one', 1)
my_map.set('two', 2)

print(my_map.get('one')) # Получение значение по ключу
print("Количество элементов в таблице:", len(my_map)) # Получение количества элементов в таблице
my_map.remove('two') # Удаление по ключу
print("Количество элементов в таблице после удаления элемента:", len(my_map))
print("Текущий уровень загруженности: ", my_map.load_factor())
