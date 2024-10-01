def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            start_byte = file.tell()
            file.write(string + '\n')
            strings_positions[(index, start_byte)] = string
    return strings_positions

# Пример использования функции
file_name = 'output.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)
print(result)