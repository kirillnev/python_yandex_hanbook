n = int(input())
for i in range(1, n + 1):
    s = []
    for j in range(1, n + 1):
        s.append(str(i * j))
    print(*s)
