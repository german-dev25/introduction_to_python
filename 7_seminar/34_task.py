"""Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Ритм есть, если число слогов (т.е. число гласных букв) в каждой
фразе стихотворения одинаковое. Фраза может состоять из одного слова,
если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Ввод в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом
все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
**Вывод:** Парам пам-пам"""

from typing import List


def count_vowel(one_phrase: list) -> int:
    vowel_letters: str = 'аеёиоуыэюя'
    phrase_vowel_count: int = 0

    for word in one_phrase:
        for char in word:
            if char.lower() in vowel_letters:
                phrase_vowel_count += 1
    return phrase_vowel_count


poem: str = input('Стихотворение: ')
vowels_of_phrases: set = set()
split_poem: List[List[str]]

# "нарезаем" стих на фразы и тут же на слова
split_poem = [word.split('-') for word in poem.strip().split()]

for phrase in split_poem:
    vowels_of_phrases.add(count_vowel(one_phrase=phrase))

print('Парам пам-пам' if len(vowels_of_phrases) == 1 else 'Пам парам')
