n = int(input('Количество элементов: '))
numbers = []
for i in range(n):
    numbers.append(int(input(f'{i + 1}-е число: ')))
print('Введенный список:', numbers)
f = numbers[0]
numbers[0] = numbers[n - 1]
numbers[n - 1] = f
print('Обновлённый список:', numbers)