numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
min_abs_val = min(numbers, key=abs)
max_abs_val = max(numbers, key=abs)
sorted_by_abs_val = sorted(numbers, key=abs)
print('Минимальный по модулю:', min_abs_val)
print('Максимальный по модулю элемент:', max_abs_val)
print('Список, отсортированный по модулю:', sorted_by_abs_val)
