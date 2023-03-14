n = int(input())
ss = []
count = 0
for i in range(n):
    ss.append([])
    while (s := input()) != 'ВСЁ':
        ss[i].append(s)
    count += 1 if 'зайка' in ss[i] else 0

print(count)
