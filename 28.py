# Задача №28. Рекурсивная функция sum(a, b), возвращающая сумму двух целых неотрицательных чисел.

A = int(input("Введите число А в рекурсивной функции: "))
B = int(input("Введите число B в рекурсивной функции: "))

def sum(A, B):
    if B == 0:
        return A
    return sum(A + 1, B - 1)

print(sum(A, B))