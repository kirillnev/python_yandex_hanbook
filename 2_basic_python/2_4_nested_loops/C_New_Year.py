n = int(input())
k = 1
i = 0
while True:
    s = []
    for j in range(i + 1):
        s.append(k)
        k += 1
        if k > n:
            break
    print(*s)
    if k > n:
        break
    i += 1
