#!/usr/bin/env python3
'''
Задание 12
Написать программу, которая спрашивает у пользователя год и определяет
является ли год високосным. (справка: В соответствии с григорианским
календарем, год является високосным, если его номер кратен 4, но не кратен
100 или кратен 400).
'''
year = input("Введите произвольный год: ")
if len(year) != 4:
    print("Введен неверный формат года. (гггг)")
else:
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        print(f"Год {year} - високосный.")
    elif year % 400 == 0:
        print(f"Год {year} - високосный.")
    else:
        print(f"Год {year} - не високосный")
