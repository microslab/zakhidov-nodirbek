#!/usr/bin/env python3
'''
Задание 3
Ввести 2 числа. Если их произведение отрицательно, умножить его на 8
и вывести на экран, в противном случае увеличить его в 1,5 раза
и вывести на экран.
'''
num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
mult = num1 * num2
if mult < 0:
    print(mult * 8)
else:
    print(mult * 1.5)
