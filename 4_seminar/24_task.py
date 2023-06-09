'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
 различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.'''

n = int(input('Ввод из нефайла количества кустов: '))
harvest = list(map(lambda k:
                   int(input(f'Урожай куста {k + 1}: ')),
                   range(n)))

max_search = []
for i in range(n - 1):
    max_search.append(harvest[i - 1] + harvest[i + 1] + harvest[i])
max_search.append(harvest[-2] + harvest[-1] + harvest[0])

print(max(max_search))
