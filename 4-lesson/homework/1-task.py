#!/usr/bin/env python3
'''
Задание 1
Составить таблицу умножения, как на картинке ниже
1   2   3   4   5   6   7   8   9
2   4   6   8   10  12  14  16  18
3   6   9   12  15  18  21  24  27
4   8   12  16  20  24  28  32  36
5   10  15  20  25  30  35  40  45
6   12  18  24  30  36  42  48  54
7   14  21  28  35  42  49  56  63
8   16  24  32  40  48  56  64  72
9   18  27  36  45  54  63  72  81
'''
for i in range(1, 10):
    print(f"{i}\t", end ='')
    for j in range(2,10):
        print(f"{i * j}\t", end='')
    print()

# old
# '''
# Задание 1
# В кругу стоят n человек, пронумерованных числами от 1 до n.
# Начинается расчет, при котором каждый k-й по счету человек выбывает из
# круга, после чего счет продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека, который останется в
# кругу последним.

# Пример: В кругу 9 человек, убывает каждый 3тий, на первом проходе уйдет
# человек под номером 3, затем 6, затем 9, затем 4, затем 8,  затем 5,
# затем 2, затем 7, последним останется человек под номером 1.
# '''
# while True:
#     players = input("Игроков: ")
#     if not players:
#         break

#     boot = input("Выбывает каждый: ")
#     if not boot:
#         print("Не введен номер выбывающего игрока. Попробуйте снова.")
#         continue

#     # check if inputs are digits
#     if players.isdigit() != True | boot.isdigit() != True:
#         print("Введены неправильные данные. Повторите снова.")
#         continue

#     # convert variables into integers
#     players = int(players)
#     boot = int(boot)

#     # Задача Иосифа Флавия
#     out = 0
#     for i in range(players,0,-1):
#         out = ((out % i) + boot - 1) % i
#         print(out)
