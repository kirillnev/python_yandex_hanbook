n = int(input())
locations = [input() for _ in range(n)]

for loc in locations:
    pos = loc.find('зайка')
    print(pos + 1 if pos != -1 else 'Заек нет =(')
