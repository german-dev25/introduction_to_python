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

from typing import List, Callable


def count_vowel(one_phrase: list) -> int:
    vowel_letters: str = 'аеёиоуыэюя'
    phrase_vowel_count: int = 0

    for word in one_phrase:
        for char in word:
            if char.lower() in vowel_letters:
                phrase_vowel_count += 1
    return phrase_vowel_count


def split_text(text: str) -> List[List[str]]:
    return [word.split('-') for word in text.strip().split()]


def rhyme_indicator(text: str,
                    counter: Callable[[List[str]], int] = count_vowel,
                    splitter: Callable[[str], List[List[str]]] = split_text,
                    ) -> int:
    vowels_of_phrases: set = set()
    for phrase in splitter(text):
        vowels_of_phrases.add(counter(phrase))
    return len(vowels_of_phrases)


def result_print(text: str, indicator=rhyme_indicator) -> None:
    print('Парам пам-пам' if indicator(text) == 1 else 'Пам парам')


def main():
    result_print(text=str(input('Стихотворение: ')))


main()
