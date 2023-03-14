a = int(input())
b = int(input())
for i in range(a):
    for j in range(b):
        offset = 1 if j == 0 else 2
        if a * b > 99:
            offset += 2
        elif a * b > 9:
            offset += 1
        print(str(i + 1 + j * a).rjust(offset), end="")
    print()
