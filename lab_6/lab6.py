# Алгоритм  Бойера-Мура
def boyer_moore_search(text, pattern):
    shift_table = {} # таблица сдвига
    '''
    В таблице сдвига определяется, на сколько позиций можно сдвинуть шаблон для дальнейшего поиска входжений
    '''
    for i in range(len(pattern)): # заполнение таблицы сдвига
        shift_table[pattern[i]] = len(pattern) - i - 1
    result_list = [] # список для хранения найенных вложений
    i = len(pattern) - 1
    while i < len(text): # проходиися по тексту с конца в начало и ищем совпадение символов, если символы не совпали, делаем сдвиг согласно таблице сдвигов
        j = len(pattern) - 1
        while text[i] == pattern[j]:
            if j == 0:
                result_list.append(i)
                break
            i -= 1
            j -= 1
        i += max(shift_table.get(text[i], len(pattern)), len(pattern) - j)
    return result_list

# Алгоритм  Рабина-Карпа
def rabin_karp_search(text, pattern):
    n = len(text) # длинна текста
    m = len(pattern) # длинна искомого слова
    pattern_hash = hash(pattern) # вычисляем хеш для искомого слова (каждой букве присваивается целое число)
    result_list = []
    for i in range(n - m + 1):
        if hash(text[i:i+m]) == pattern_hash: # вычисляем хеш выделенной подстроки
            if text[i:i+m] == pattern: # сравниваем вычисленный хеш с искомым (сравниваются последовательности цифр или числа)
                result_list.append(i) # если текущий хеш и искомый совпали, записываем в результат ,
    return result_list

# Алгоритм  Кнута-Морриса-Пратта
def kmp_search(text, pattern):
    lps = [0] * len(pattern) # переменная для хранения префикса, суффикса
    i = 1
    j = 0
    result_list = []
    while i < len(pattern): # проходимся по искомому слову
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j # записываем символ
            i += 1
        else:
            if j != 0: # если есть более короткое совпадение, записываем его
                j = lps[j-1]
            else: # иначе записываем найденное совпадение
                lps[i] = 0
                i += 1
    # после поиска преффикса\суффикса используем lps для поиска подстроки
    i = 0
    j = 0
    '''
    Далее переменная i используется для перебора букв в тексте, а j в шаблоне
    '''
    while i < len(text): # пока строка не закончилась
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern): # если найдена подстрока, записываем индекс вхождения
            result_list.append(i-j)
            j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0: # проверяем, можно ли взять более короткий префикс\суффикс
                j = lps[j-1] # если можно, делаем это
            else: # если нельзя, переходим к следующей букве
                i += 1
    return result_list


if __name__ == "__main__":
    print("Алгоритм  Бойера-Мура")
    text = "Шёл медведь по лесу, увидел горящую машину. Сел в неё и сгорел"
    pattern = "медведь"
    result = boyer_moore_search(text.lower(), pattern)
    print("Исходный текст: " + text + "\nИскомое слово: " + pattern + "\nВхождения: ")
    print(result)

    print("\nАлгоритм  Рабина-Карпа")
    text = "Шёл медведь по лесу, видит — машина горит. Только хотел в неё сесть, а там уже другой медведь горит."
    pattern = "медведь"
    result = rabin_karp_search(text.lower(), pattern)
    print("Исходный текст: " + text + "\nИскомое слово: " + pattern + "\nВхождения: ")
    print(result)

    print("\nАлгоритм  Кнута-Морриса-Пратта")
    text = "Мужчина в Древнем Риме заходит в бар, поднимает 2 пальца и говорит:-Мне 5 кружек пива, пожалуйста"
    pattern = "пальца"
    result = kmp_search(text.lower(), pattern)
    print("Исходный текст: " + text + "\nИскомое слово: " + pattern + "\nВхождения: ")
    print(result)
