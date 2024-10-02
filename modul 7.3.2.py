import os
import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r') as file:
                    words = []
                    for line in file:
                        line = line.lower()  # Приводим строку к нижнему регистру
                        line = line.translate(str.maketrans('', '', string.punctuation + ' -'))
                        words.extend(line.split())  # Разбиваем строку на слова
                    all_words[file_name] = words  # Записываем слова в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Индекс по умолчанию увеличивается на 1

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result


# Пример использования
if __name__ == "__main__":
    print("Текущая рабочая директория:", os.getcwd())
    finder = WordsFinder('C:/Users/user/PycharmProjects/pythonProject/file1.txt',
                         'C:/Users/user/PycharmProjects/pythonProject/file2.txt',
                         'C:/Users/user/PycharmProjects/pythonProject/file3.txt')

    print(finder.get_all_words())
    print(finder.find('someword'))
    print(finder.count('someword'))
