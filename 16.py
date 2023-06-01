# Задача №16. Сколько раз элемент встречается в массиве.

import random

n = int(input("Введите натуральное число N - размер массива: "))
a = []
for i in range(n):
    a.append(random.randint(0, 50))
print(a)
x = int(input("Введите натуральное число X: "))
print(a.count(x))