name = input()
price = int(input())
weight = int(input())
n = int(input())

change = n - price * weight
print('Чек')
print(f'{name} - {weight}кг - {price}руб/кг')
print(f'Итого: {weight * price}руб')
print(f'Внесено: {n}руб')
print(f'Сдача: {change}руб')