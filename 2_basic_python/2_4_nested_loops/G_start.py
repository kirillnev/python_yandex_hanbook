n = int(input())
s = 3
for i in range(n):
    for j in range(s, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')
    s += 1
