# a and b орел и решка на монетке

import random

w = int(input("Введите число монеток: "))
a = 0 
coins = []
for i in range(w):
    coins.append(random.randint(0, 1))

print(f"такие монеты выпали: {coins}")
a = sum(coins)
b = w - a

if a < b:
    print(f"Нам нужно перевернуть {a} монеток, которые лежат вверх орлом.")
elif a > b:
    print(f"Нам нужно перевернуть {b} монеток, которые лежат вверх решкой.")
elif a == 0 or a == w:
    print("Не нужно переворачивать монеты.")
elif a == b:
    print(f"Не важно какие монетки переворачивать. Их одинаковое количесво = {a}.")