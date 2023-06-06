# Задача №22. Выдать без повторений числа из двух рандомных наборов чисел.

import random

n = int(input("Введите длину первого массива: "))
a = []
for i in range (n):
    a.append(random.randint(0, 10))
print(a)

m = int(input("Введите длину второго массива: "))
b = []
for i in range (n):
    b.append(random.randint(0, 10))
print(b)

my_list = [sorted(a + b)]
print(list(set(sorted(a + b))))

