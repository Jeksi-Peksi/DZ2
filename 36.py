# Задача №36. Выводим таблицу

def print_operation_table(operation, num_rows=10, num_columns=10):
    f = [[operation(a, b) for a in range(1, num_rows + 1)] for b in range(1, num_columns + 1)]
    for a in f:
        print(*[f"{x}"for x in a])

print_operation_table(lambda x, y: x * y)