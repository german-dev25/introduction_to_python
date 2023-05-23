""" Задача 36: Напишите функцию print_operation_table(operation, num_rows=6,
num_columns=6), которая принимает в качестве аргументОВ:
- функцию, вычисляющую элемент по номеру строки и столбца
- аргументы num_rows и num_columns, указывающие число строк и столбцов таблицы,
которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы
(подумайте, почему не с нуля (потому :))).

Примечание: бинарной операцией называется любая операция, у которой ровно
два аргумента, как, например, у операции умножения.
еще есть, тогда уж, тернарная - там ровно три "аргумента"
и есть еще и унарная операция - унарный плюс тот же самый.

*Пример:*

**Ввод:**
`print_operation_table(lambda x, y: x * y)`
**Вывод:**
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""

from typing import Callable


def print_operation_table(operation: Callable[[int, int], int],
                          num_rows: int = 6,
                          num_columns: int = 6) -> None:
    for i in range(1, num_rows + 1):
        row = ""
        for k in range(1, num_columns + 1):
            row += str(operation(i, k)).center(5)
        print(row)
    print(sep='\n')


def addition(x: int, y: int) -> int:
    return x + y


print_operation_table(lambda x, y: x * y)
print_operation_table(addition, num_rows=5, num_columns=5)
