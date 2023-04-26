'''Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random

num_list = [random.randint(1, 100) for _ in range(10)]

num_range = [
    int(input('Введите начало диапазона: ')),
    int(input('Введите конец диапазона: '))
]
result = [index for index, num in enumerate(num_list)
          if num_range[0] <= num <= num_range[1]]

print(f'Индексы элементов, значения которых в диапазоне '
      f'[{num_range[0]}:{num_range[1]}]: {result}')