#!/usr/bin/env python3
# Кортежи/множества
'''
Задание 7
Есть кортеж с данными numbers = (12, 33, 44, 33, 12, 45, 11, 55, ’44’, 30, 10),
создайте список и кортеж данных без дубликатов
'''
numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
setnum = set(numbers)
tupnum = tuple(numbers)

print(setnum)
