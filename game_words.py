from utils import *

basic_word = load_random_word()
name = input("Введите имя игрока\n")
player = Player(name)

print(f"Привет, {player.name}!\n"
      f"Составьте {basic_word.word_count} слов из слова: {basic_word.word.upper()}\n"
      f"Слова должны быть не короче {basic_word.small_word} букв\n"
      f'Чтобы закончить игру, угадайте все слова или напишите "стоп"')

for i in range(basic_word.word_count):  # цикл количества под_слов
    while True:  # Цикл будет ожидать правильный ответ пользователя
        answer_user = input("Введите слово:\n").lower().strip()
        if answer_user in ("стоп", "stop"):
            print(f"Игра окончена!\nВы угадали {player.use_sub_words_count} слов")
            quit()
        elif len(answer_user) < basic_word.small_word:
            print("Слишком короткое слово")
        elif basic_word.sub_words_true(answer_user) and not player.use_sub_words_true(answer_user):
            print("Верно")
            player.add_word(answer_user)
            break
        elif player.use_sub_words_true(answer_user):
            print("Вы уже использовали такое слово")
        else:
            print("Неверно")

print(f"Игра окончена!\nВы угадали {player.use_sub_words_count} слов")
