# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

# принимаем строку и преобразовываем ее в список из "0" и "1"
coins_list = list(
    filter(lambda x: x == "0" or x == "1",
           input("Ввод данных, где 0 - решка, 1 - орел: "))
)

# Вариант 1: Цикл for
tails, eagles = 0, 0
for coin in coins_list:
    if coin == "1":
        eagles += 1
    else:
        tails += 1
print(eagles if eagles < tails else tails)

# Вариант 2: Методы списка
tails, eagles = coins_list.count("0"), coins_list.count("1")
print(eagles if eagles < tails else tails)
