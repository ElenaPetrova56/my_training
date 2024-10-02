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
                        # Удаляем пунктуацию
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
                # Позиция слова в списке увеличена на 1 для соответствия естественной нумерации
                result[file_name] = words.index(word) + 1

        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result


# Пример использования:
if __name__ == "__main__":
    finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
    # Получаем все слова
    print(finder.get_all_words())
    # Находим первое вхождение слова
    print(finder.find('someword'))
    # Считаем количество вхождений слова
    print(finder.count('someword'))
