# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

users_number = input("Введите число: ")

if not users_number.isdigit():
    print("Нужно ввести число")
elif len(users_number) != 3:
    print("Нужно ввести трехзначное число")
else:
    # Вариант 1 - математический
    users_number = int(users_number)
    first_digit = users_number // 100           # первая цифра
    second_digit = (users_number // 10) % 10    # вторая цифра
    third_digit = users_number % 10             # третья цифра
    result = first_digit + second_digit + third_digit

    # # Вариант 2 - извлекаем из строки по индексу
    # result = 0
    # first_digit = users_number[0]
    # second_digit = users_number[1]
    # third_digit = users_number[2]
    # result = int(first_digit) + int(second_digit) + int(third_digit)

    # # Вариант 3 - цикл
    # result = 0
    # for digit in users_number:
    #     result += int(digit)

    # Вывод результата
    print(result)
