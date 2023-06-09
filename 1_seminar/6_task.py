# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no


# # выполнение проверок введеного числа не делалась
# Вариант 1 - математический
ticket_number = int(input("Введите 6-значный номер билета: "))

left_sum = ticket_number // 100000 \
           + ticket_number // 10000 % 10 \
           + ticket_number // 1000 % 10
right_sum = ticket_number % 1000 // 100 \
            + ticket_number % 100 // 10 \
            + ticket_number % 10

print("Счастливый билет" if left_sum == right_sum else "Несчастливый билет")

# # Вариант 2 - используя строки
# ticket_number = int(input("Введите 6-значный номер билета: "))
# left_sum = int(str(ticket_number)[0]) \
#            + int(str(ticket_number)[1]) \
#            + int(str(ticket_number)[2])
# right_sum = int(str(ticket_number)[3]) \
#             + int(str(ticket_number)[4]) \
#             + int(str(ticket_number)[5])
# print("Счастливый билет" if left_sum == right_sum else "Несчастливый билет")