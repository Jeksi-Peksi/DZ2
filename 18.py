# Задача №18. Найти в массиве самый близкий по величине к числу Х.

import random

n = int(input("Введите натуральное число N - размер массива: "))
a = []
for i in range(n):
    a.append(random.randint(0, 101))
print(a)
a.sort()
print(a)
x = int(input("Введите натуральное число X: "))
for i in range(n):
    if a[i] - x < 0:
        b = a[i]
        c = a[i + 1]
        quit
if x - b == c - x:
    print("Число", x, "ближе всего к двум числам из массива: ", b, "и", c)
else:
    if x - b > c - x:
        print("Число", x, "ближе всего к числу", c, "из массива.")
    else:
        print("Число", x, "ближе всего к числу", b, "из массива.")
