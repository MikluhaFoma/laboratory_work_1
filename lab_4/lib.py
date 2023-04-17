class HashMap:
  def __init__(self):
      #Инициализация хэш-таблицы
      self.capacity = 50 # Максимальное количество элементов в хэш-таблице
      self.size = 0 # Текущее количество элементов в хэш-таблице
      self.keys = [None]*self.capacity # Массив ключей
      self.values = [None]*self.capacity # Массив значений

  def hash(self, key): # Хэш-функция
      hashsum = 0
      for idx, c in enumerate(key): # Получаем индекс и значение ключа
          hashsum += (idx + len(key)) ** ord(c)
          hashsum = hashsum % self.capacity # Получение индекса элемента в хэш-таблице
      return hashsum # Возвращаем вычисленное значение

  def set(self, key, value): # Метод добавление элемента
      if self.size == self.capacity:
          raise Exception('Хэш-таблица заполнена') # Если хэш-таблица заполнена, выбрасываем исключение
      index = self.hash(key) # Получение индекса элемента в хэш-таблице
      while self.keys[index] is not None: # Пока не найдено свободное место для элемента
          if self.keys[index] == key: # Если ключ уже есть в хэш-таблице
              self.values[index] = value # Обновляем значение элемента
              return
          index = (index + 1) % self.capacity # Используем метод линейного опробования для разрешения коллизий
      self.keys[index] = key # Добавляем ключ в хэш-таблицу
      self.values[index] = value # Добавляем значение элемента в хэш-таблицу
      self.size += 1 # Увеличиваем количество элементов в хэш-таблице

  def get(self, key): # Получение значения элемента
      index = self.hash(key) # Получение индекса элемента в хэш-таблице
      while self.keys[index] is not None: # Пока не найдено значение элемента или свободное место
          if self.keys[index] == key: # Если ключ найден
              return self.values[index] # Возвращаем значение элемента
          index = (index + 1) % self.capacity # Используем метод линейного опробования для разрешения коллизий
      return None # Если ключ не найден, возвращаем None

  def delete(self, key): # Удаление элемента
      index = self.hash(key) # Получение индекса элемента в хэш-таблице
      while self.keys[index] is not None: # Пока не найдено значение элемента или свободное место
          if self.keys[index] == key: # Если ключ найден
              self.keys[index] = None # Удаляем ключ
              self.values[index] = None # Удаляем значение элемента
              self.size -= 1 # Уменьшаем количество элементов в хэш-таблице
              return
          index = (index + 1) % self.capacity # Используем метод линейного опробования для разрешения коллизий
      return None # Если ключ не найден, возвращаем None
