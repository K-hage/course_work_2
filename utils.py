import requests
from random import choice
from classes import *


def load_random_word():
    """Получаем список с внешнего ресурса, берем случайное слово"""

    response = requests.get('https://jsonkeeper.com/b/KTJB')
    json_list = response.json()
    random_dict = choice(json_list)
    word, sub_words = random_dict.values()
    return BasicWord(word, sub_words)

