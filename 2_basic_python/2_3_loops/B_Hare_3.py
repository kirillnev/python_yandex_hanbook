count = 0
while (s := input()) != 'Приехали!':
    count += 1 if 'зайка' in s else 0

print(count)
