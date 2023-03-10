# Zakhidov Nodirbek
'''
Задание 1
Дано целое число. Если оно является положительным то прибавить к нему 20,
в противном случае вычесть из него 5. Вывести полученное число
'''
num = int(input("Введите число: "))
if num > 0:
    num = num + 20
elif num < 0:
    num = num - 5
print(num)

'''
Задание 2
Дано 2 числа. Если их сумма кратна 5, прибавить 1, иначе вычесть 2
'''
#      float()?
num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
sum = num1 + num2
print(sum + 1 if sum % 5 == 0 else sum - 2)

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

'''
Задание 4
Составить программу, которая запрашивает ввод температуры тела человека и
определяет, здоров он или болен
'''
temp = float(input("Введите температуру: "))
# reference
# https://wikipedia.org/wiki/Human_body_temperature
print("Вы здоровы" if 37.5 > temp > 35.0 else "Срочно к врачу")

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

'''
Задание 6
Составить программу чтобы компьютер запросил имя пользователя и его год
рождения, затем подсчитал возраст человека, в зависимости от года рождения.
'''
from datetime import datetime

name = input("Введите имя: ")
year = int(input("Введите год рождения: "))

age = datetime.now().year - year
print(f"Привет {name}, тебе {age}.")

'''
Задание 7
Программа спрашивает возраст пользователя.
— Если возраст меньше или равен 18, то вывести: «Вам нужно учиться».
— Если возраст больше 18, но меньше или равен 50 — «Вам нужно работать»
— Если возраст больше 50, но меньше или равен 59 — «Вам скоро на пенсию»
— Если возраст больше 59, но меньше 110 — «Вы пенсионер».
'''
age = int(input("Введите ваш возраст: "))
if age < 1:
    print("Вам нужно родиться")
elif age <= 18:
    print("Вам нужно учиться")
elif age <= 50:
    print("Вам нужно работать")
elif age <= 59:
    print("Вам скоро на пенсию")
elif age <= 110:
    print("Вы пенсионер")
else:
    print("Вы пенсионер - Дракула")

'''
Задание 8
 Напишите программу, которая принимает целое число от 1 до 12 и возвращает
 название месяца и количество дней.
'''
monthnum = int(input("Введите номер месяца: "))

if monthnum == 2:
    days = "28 или 29"
elif monthnum == 12:
    days = "31"
elif monthnum % 2 == 0:
    days = "30"
else:
    days = "31"

# Словарь нужен ой как
if monthnum == 1:
    month = "Январь"
elif monthnum == 2:
    month = "Февраль"
elif monthnum == 3:
    month = "Март"
elif monthnum == 4:
    month = "Апрель"
elif monthnum == 5:
    month = "Май"
elif monthnum == 6:
    month = "Июнь"
elif monthnum == 7:
    month = "Июль"
elif monthnum == 8:
    month = "Август"
elif monthnum == 9:
    month = "Сентябрь"
elif monthnum == 10:
    month = "Октябрь"
elif monthnum == 11:
    month = "Ноябрь"
elif monthnum == 12:
    month = "Декабрь"
else:
    print("Введен неверный месяц!")
    exit

print(f"Название месяца: {month}. Количество дней: {days}")

'''
Задание 9
Написать программу, которая спрашивает у пользователя три числа
и выводит количество совпадающих.
'''

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

match = 0

if num1 == num2:
    match = 2
if num2 == num3:
    match = 2
if num3 == num1:
    match = 2

if num1 == num2 == num3:
    match = 3

print(f"Количество совпадающих чисел: {match}")

'''
Задание 10
Если заданы два целых числа, они возвращают свое произведение только
в том случае, если произведение не больше 1000, иначе возвращают свою сумму.
'''
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 * num2 < 1000:
    print(f"Результат {num1 * num2}")
else:
    print(f"Результат {num1 + num2}")

'''
Задание 11
Напишите программу для отображения «Hello», если введенное пользователем
число кратно пяти, в противном случае выведите «Bye».
'''

num = int(input("Введите число: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

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

'''
Задание 13
Шоколадка имеет вид прямоугольника, разделенного на width×length долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите, можно ли таким образом отломить от шоколадки часть, состоящую
ровно из x долек. Программа получает на вход три числа: width, length, parts
и должна вывести YES или NO. (учтите что пользователь может ввести не
правильные параметры, ваша программа не должна вылетать с ошибкой)

                     length
+-----+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |     | w
|     |     |     |     |     |     |     |     | i
+-----+-----+-----+-----+-----+-----+-----+-----+ d
|     |     |     |     |     |     |     |     | t
|     |     |     |     |     |     |     |     | h
+-----+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+-----+
'''
width = input("Введите width: ")
length = input("Введите length: ")
parts = input("Введите parts: ")

if not width.isdigit() or not length.isdigit() or not parts.isdigit():
    print("Error. Input values are not digits!")
    exit()

if int(parts) > (int(length) * int(width)):
    print("Error. Impossible amount of parts")
    exit()

if (int(parts) % int(width)) == 0 or (int(parts) % int(length)) == 0:
    print("YES")
else:
    print("NO")
