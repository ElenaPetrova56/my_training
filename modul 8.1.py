def add_everything_up(a, b):
    try:
        # Если оба аргумента являются числами, складываем их
        return a + b
    except TypeError:
        # Если возникает ошибка, возвращаем строковое представление
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))      # яблоко4215
print(add_everything_up(123.456, 7))           # 130.456