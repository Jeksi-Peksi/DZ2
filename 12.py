# Задача №12. Про Петю и Катю.


S = int(input("Какая сумма двух чисел? "))
P = int(input("Какое произведение двух чисел? "))

for a in range(S):
    for b in range(P):
        if S == a + b and P == a * b:
            print(a, b)