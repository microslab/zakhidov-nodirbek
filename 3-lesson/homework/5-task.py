#!/usr/bin/env python3
'''
Задание 5
Составить программу, которая запрашивает ввод трех значений температуры
и проверяет, есть ли среди них температура таяния льда.
Если такая температура введена, вывести на экран сообщение
«Введена температура таяния льда», иначе «Такой температуры нет»
'''
temp1 = float(input("Введите температуру 1: "))
temp2 = float(input("Введите температуру 2: "))
temp3 = float(input("Введите температуру 3: "))
if temp1 > 0 or temp2 > 0 or temp3 > 0:
    print("Введена температура таяния льда")
else:
    print("Такой температуры нет")
