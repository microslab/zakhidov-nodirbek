#!/usr/bin/env python3
'''
Задание 1
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые
больше 5.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for i in a:
    if i <= 5:
        b.append(i)
    else:
        c.append(i)

print(f"Список чисел меньше или равных 5 {b}")
print(f"Список чисел больше 5 {c}")