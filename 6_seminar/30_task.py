'''Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

text_for_user = ['Введите первый элемент: ',
                 'Введите разность: ',
                 'Введите количество элементов: ']

# формируем список из ответов пользователя (только из интереса делал так)
data = list(map(lambda i: int(input(i)), text_for_user))

progression = [data[0] + (i * data[1]) for i in range(data[2])]
print('Арифметическая прогрессия: ', *progression)
