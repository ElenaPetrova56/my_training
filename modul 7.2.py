import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r') as file:
                    content = file.read().lower()
                    for p in punctuations:
                        content = content.replace(p, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        word_positions = {}

        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word)
            else:
                word_positions[file_name] = -1

        return word_positions

    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        word_counts = {}

        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)

        return word_counts


# Пример использования
if __name__ == "__main__":
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    finder = WordsFinder(*files)

    # Получение всех слов из файлов
    all_words = finder.get_all_words()
    print("Все слова из файлов:", all_words)

    # Поиск слова в файлах
    word_to_find = 'example'
    word_positions = finder.find(word_to_find)
    print(f"Позиции слова '{word_to_find}' в файлах:", word_positions)

    # Подсчёт слова в файлах
    word_to_count = 'example'
    word_counts = finder.count(word_to_count)
    print(f"Количество слова '{word_to_count}' в файлах:", word_counts)
