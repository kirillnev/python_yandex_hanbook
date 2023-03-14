a = int(input())
b = int(input())
k = 1
for i in range(a):
    for j in range(b):
        offset = 1 if j == 0 else 2
        if a * b > 99:
            offset += 2
        elif a * b > 9:
            offset += 1
        print(str(k).rjust(offset), end="")
        k += 1
    print()
