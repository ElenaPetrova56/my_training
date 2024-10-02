first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, где длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Список кортежей пар слов одинаковой длины
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Словарь с парой ключ-значение: строка-длина строки
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример вывода
print(first_result)
print(second_result)
print(third_result)


