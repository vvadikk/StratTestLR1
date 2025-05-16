def sum_1(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (i ** 2)
    return s
def sum_2(n, m):
    s = 0
    for i in range(1, m + 1):
        s += i ** n
    return s
def select_operation(operation):
    if operation == 1:
        return sum_1
    elif operation == 2:
        return sum_2
operation1 = select_operation(1)
operation2 = select_operation(2)
print('Операция 1 от 3:', operation1(3))
print('Операция 2 от (3, 3):', operation2(3, 3))
