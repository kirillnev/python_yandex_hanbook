name = input()
price = int(input())
weight = int(input())
n = int(input())

change = n - price * weight
price_str = f'{weight}кг * {price}руб/кг'
all_str = f'{weight * price}руб'
n_str = f'{n}руб'
change_str = f'{change}руб'
print('================Чек================')
print('Товар:', name.rjust(28))
print('Цена:', price_str.rjust(29))
print('Итого:', all_str.rjust(28))
print('Внесено:', n_str.rjust(26))
print('Сдача:', change_str.rjust(28))
print('===================================')
