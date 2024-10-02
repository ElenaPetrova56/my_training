def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += num  # Попытка прибавить число
        except TypeError:
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных

    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        # Проверяем, является ли входной параметр коллекцией
        if not isinstance(numbers, (list, tuple)):
            raise TypeError

        # Получаем сумму и количество некорректных данных
        total_sum, incorrect_data = personal_sum(numbers)

        # Обрабатываем случай деления на 0
        average = total_sum / (len(numbers) - incorrect_data)
        return average

    except ZeroDivisionError:
        return 0  # Если деление на 0, возвращаем 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

# Примеры использования функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
