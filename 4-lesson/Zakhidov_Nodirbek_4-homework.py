# Zakhidov Nodirbek
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

'''
Задание 2
Составить программу, которая спрашивает возраст человека и, если ему 18 лет
и больше, сообщает “Замечательно. Вы уже можете водить автомобиль”, а в
противном случае – “К сожалению, водить автомобиль Вам рановато”.
(так же можете сами придумать и добавить вывод сообщения в
 зависимости от возраста)
'''
while True:
    age = input("Введите ваш возраст: ")
    if not age:
        break

    if age.isdigit() != True:
        print("Введены неправильные данные. Повторите снова.")
        continue

    age = int(age)

    if age < 1:
        print("Вам надо сначала родиться, чтобы водить что-то.")
    elif age < 17:
        print("Вам еще рано водить что-либо на дороге.")
    elif age < 19:
        print("Вам можно водить мотоциклы и мопеды.")
    elif age < 22:
        print("Вам можно водить автомобиль.")
    elif age < 80:
        print("Вам можно водить автомобиль, автобус и даже трамвай.")
    elif age < 130:
        print("Вы уверены что хотите что-то водить?")
    else:
        print("Неверный диапазон возраста.")

    cont = input("Продолжим? [Y/n]")
    if not cont:
        continue
    elif cont.lower()[:1] == 'y':
        continue
    elif cont.lower()[:1] == 'n':
        print("Выход.")
        break

'''
Задание 3
Создайте игру «Угадай число», программа генирирует рандомное число в заданном
интервале, и предлагает пользователю угадать, игра продолжается до тех пор
пока пользователь угадает число, пример игры на картинке ниже:
    Python: Привет, как тебя зовут?
    Ваше имя: Хасан
    Python: Что ж, Хасан, я загадываю число от 1 до 5.
    Python: Попробуй угадать.
    Хасан: 5
    Python: Твое число слишком большое.
    Python: Попробуй угадать.
    Хасан: 1
    Python: Твое число слишком маленькое.
    Python: Попробуй угадать.
    Хасан: 3
    Python: Отлично, Хасан! Ты справился за 3 попытки.

можете сделать таймер
сделайте игру по уровням, первый уровень с 1 до 5,
второй уровень с 1 до 10 и.т.д.

'''
from random import randrange

while True:
    print("Python: Привет, как тебя зовут?")
    name = input("Ваше имя: ")
    if not name:
        break

    level = 1
    while True:
        maximum = 5 * level
        print("-"*20)
        print(f"Python: Уровень {level}")
        print(f"Python: Что ж, {name}, я загадываю целое число от 1 до {maximum}.")
        number = randrange(1, maximum + 1)
        att = 0

        while True:
            print("Попробуй угадать.")
            guess = input(f"{name}: ")
            att += 1

            if guess.isdigit() != True:
                print("Это не номер. Повторите снова.")
                continue

            guess = int(guess)
            if guess == number:
                print(f"Python: Отлично, {name}! Ты справился за {att} попытки.")
                cont = input("Python: Перейти на следующий уровень? [Y/n]")
                if not cont:
                    level += 1
                    break
                elif cont.lower()[:1] == 'y':
                    level += 1
                    break
                elif cont.lower()[:1] == 'n':
                    print(f"Python: Вы дошли до {level}-го уровня.")
                    exit()
            elif guess > number:
                print("Твое число слишком большое.")
            else:
                print("Твое число слишком маленькое.")

'''
Задание 4
Многие спортсмены жаловались, что судья слишком тихо отсчитывает секунды,
оставшиеся до старта («Три!.. Два!.. Один!..»). Фирма Go Ahead купила табло
для наглядного отображения оставшегося времени.

Запрограммируйте табло так, чтобы оно по порядку печатало, сколько секунд
осталось

Укажите время для таймера (в минутах): 240
2 : 59 : 52
'''
import datetime
from time import sleep

data = int(input("Укажите время для таймера (в минутах): "))
# Конвертация минут в ЧАС:МИНУТА:СЕКУНДА
timer = str(datetime.timedelta(minutes=data))

h, m, s = timer.split(":")  # Распаковка элементов списка
h, m, s = int(h), int(m) - 1, int(s)  # всегда должно быть на минуту меньше

if m == -1:
    m = 59
    h -= 1

for k in range(h,-1,-1):
    for j in range(m,-1,-1):
        for i in range(60,-1,-1):
            print(f"\r{k}:{j}:{i}", end='', flush=True)
            sleep(1)
    m = 59

'''
Задание 5
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с
шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется
написать программу, которая выводит на экран все доступные счастливые билеты
с подсчетом их количества.
'''
lucky = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if a + b + c == d + e + f:
                            print(f"Счастливый билет №{lucky}:  {a} {b} {c} {d} {e} {f}")
                            lucky += 1
print(f"Количество счастливых билетов: {lucky}")
print(f"Всего {round(lucky * 100 / 999999, 2)} %")

'''
Задание 6
Нарисуйте ёлку (вид ёлки произвольный), высоту ёлки должен задавать
пользователь
'''
while True:
    size = input("Высота елки: ")
    if size.isdigit():
        size = int(size)
        break
    else:
        continue

for i in range(size):
    # пустота
    print(" " * (size - i - 1), end="")

    # горизонталь
    rn = 2 * i + 1

    for j in range(rn):
        if i == 0:
            print("*", end="")
        elif j == 0:
            print("/", end="")
        elif j == rn - 1:
            print("\\", end="")
        else:
            print("#", end="")
    print()

if size > 5:
    print(" " * int(j/2 - 1), end="")
    print("| |")
else:
    print(" " * int(j/2), end="")
    print("|")

'''
Задание 7
Написать программу «Банк». Вводится сумма вклада и количество лет. Рассчитать
сколько денег будет на счету пользователя к концу времени вклада. Решить
задачу по системе «сложный процент» (процент рассчитывается от новой суммы)
Годовой процент считать равным 10%.
'''

while True:
    money = input("Введите сумму вклада: ")
    years = input("Введите количество лет для вклада: ")
    if money.isdigit() and years.isdigit():
        money = float(money)
        years = int(years)
        break
    else:
        continue

percent = 1.1
for i in range(1, years + 1):
    money = money * percent
    print(f"{round(years, 2)} год: {round(money, 2)} $")

print(f"За {round(years, 2)} лет вы соберете: {round(money, 2)} $")

'''
Задание 8
Задача «Лесенка» По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов.
'''
while True:
    quant = input("Введите количество лесенок: ")
    if quant.isdigit():
        quant = int(quant)
        break
    else:
        continue

for i in range(1, quant + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

'''
Задание 9
Последовательность Фибоначчи — это серия чисел. Следующее число находится
путем сложения двух чисел перед ним. В первые два числа 0 и 1 .
Например, 0 + 1 = 1
'''
while True:
    last = input("Конечный нормер Фибоначчи: ")
    if last.isdigit():
        last = int(last)
        break
    else:
        continue

a = 0
b = 1
print('0',end=' ')
while b < last + 1:
    a, b = b, a + b
    print(a,end=' ')
print()
