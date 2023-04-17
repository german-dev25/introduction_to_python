# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

n = int(input("Введите количество элементов в массиве: "))
search_num = int(input("Введите искомое число: "))

# генератор списка, заполняемый рандомно
random_num_list = [random.randint(1, 100) for _ in range(n)]

nearest_num = random_num_list[0]
for list_num in random_num_list:
    if abs(list_num - search_num) < abs(nearest_num - search_num):
        nearest_num = list_num

print(f"Получившийся массив {random_num_list} \n"
      f"Ближайшее к числу {search_num} число в массиве: {nearest_num}")
