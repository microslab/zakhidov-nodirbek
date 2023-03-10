#!/usr/bin/env python3
# Вложенность
'''
Задание 2
Есть словарь кодов товаров и словарь количества товара на складе, задача
сопоставить два словаря и высчитать общее количество.
'''
goods = {
 'Лампа': '12345',
 'Стол': '23456',
 'Диван': '34567',
 'Стул': '45678',
}

store = {
 '12345': [
  {
   'quantity': 27,
   'price': 42
  },
 ],
 '23456': [
  {
   'quantity': 22,
   'price': 510
  },
  {
   'quantity': 32,
   'price': 520
  },
],
 '34567': [
  {
   'quantity': 2,
   'price': 1200
  },
  {
   'quantity': 1,
   'price': 1150
  },
 ],
 '45678': [
  {
   'quantity': 50,
   'price': 100
  },
  {
   'quantity': 12,
   'price': 95
  },
  {
   'quantity': 43,
   'price': 97
  },
 ],
}
# кода намного меньше, чем ожидалось
for i in goods:
    quant = price = 0
    for j in range(len(store[goods[i]])):
        quant += store[goods[i]][j]['quantity']
        price += store[goods[i]][j]['price'] * store[goods[i]][j]['quantity']

    print(f"Продукт: {i}, Количество: {quant}, Стоимость: {price}")
