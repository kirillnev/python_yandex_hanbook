x = 0
y = 0
while (command := input()) != 'СТОП':
    n = int(input())
    if command == 'ВОСТОК':
        x += n
    elif command == 'ЗАПАД':
        x -= n
    elif command == 'СЕВЕР':
        y += n
    elif command == 'ЮГ':
        y -= n

print(y, x, sep="\n")
