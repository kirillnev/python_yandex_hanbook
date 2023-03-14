name = input()
m = int(input())

print(f'Группа №{m // 100}.')
print(f'{m % 10}. {name}.')
print(f'Шкафчик: {m}.')
print(f'Кроватка: {(m % 100) // 10}.')