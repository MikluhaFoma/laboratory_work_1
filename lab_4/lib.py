class hash_map: # Определение класса hash_map
    def __init__(self, max_load_factor = 2.0): # Конструктор класса, инициализирует хеш-таблицу с пустыми списками
        self.size = 0
        self.capacity = 8 # Начальная емкость хеш-таблицы
        self.max_load_factor = max_load_factor
        self.buckets = [[] for _ in range(self.capacity)]

    def clear(self): # Метод для удаления всех элементов из хеш-таблицы
        self.size = 0
        self.capacity = 8
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_function(self, key):
        return hash(key) % self.capacity

    def set(self, key, value): # Метод добавления элемента в таблицу
        bucket = self.buckets[self.hash_function(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1
            if self.size / self.capacity > self.max_load_factor:
                self._resize()

    def remove(self, key): # Метод для удаления элемента по ключу
        bucket = self.buckets[self.hash_function(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)

    def get(self, key, default = None):# Метод получения значения по ключу
        bucket = self.buckets[self.hash_function(key)]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def __len__(self): # Метод для получения количества элементов в хеш-таблице
        return self.size

    def load_factor(self): # Метод для получения текущего уровня загруженности хеш-таблицы
        return self.size / self.capacity

    def _resize(self): # Метод для изменения коэффициента загрузки хеш-таблицы и перехеширования всех элементов хеш-таблицы
        self.capacity = self.capacity * 2 + 1
        new_buckets = [[] for _ in range(self.capacity)]
        for bucket in self.buckets:
            for k, v in bucket:
                new_buckets[self.hash_function(k)].append((k, v))
        self.buckets = new_buckets
