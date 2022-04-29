class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def sub_words_true(self, answer_user):
        """Проверка в списке допустимых под_слов"""

        return answer_user in self.sub_words

    @property
    def word_count(self):
        """Считает количество под_слов"""

        return int(len(self.sub_words))

    @property
    def small_word(self):
        """Возвращает длину самого короткого слова в списке под_слов"""

        return int(len(min(self.sub_words, key=len)))


class Player:

    def __init__(self, name):
        self.name = name
        self.use_sub_words = []

    @property
    def use_sub_words_count(self):
        """Получение количества слов"""

        return int(len(self.use_sub_words))

    def add_word(self, add_word):
        """Добавление слова в список угаданных слов"""

        self.use_sub_words.append(add_word)

    def use_sub_words_true(self, answer_user):
        """Проверка использования данного слова ранее"""

        return answer_user in self.use_sub_words
