# Задача №14. Вывести все целые степени двойки (2k), не превосходящие N.

n = int(input("Введите любое число, но не сильно большое, чтобы пересчитывать было не сложно. Желательно кратное 2-м: "))
k = 0
while 2 ** k <= n:
    print(2 ** k)
    k += 1