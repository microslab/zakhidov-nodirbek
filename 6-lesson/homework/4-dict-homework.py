#!/usr/bin/env python3
# Словари
'''
Задание 4
Напишите код для объединения двух списков в словарь ключ: значение.
СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)
'''
ips = ['192.168.20.1', '10.10.30.25', '172.16.3.40']
users = ['Вася Пупкин', 'Денис Уткин', 'Саша Дудкин']
userip = {}

for i in range(len(ips)):
    userip.update({users[i]: ips[i]})

print(userip)
