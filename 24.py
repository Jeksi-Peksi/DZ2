n = int(input("Всего кустов на грядке: "))
arr = list()
for i in range(n):
    x = int(input("Сколько ягод выросло на кусте?: "))
    arr.append(x)
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))