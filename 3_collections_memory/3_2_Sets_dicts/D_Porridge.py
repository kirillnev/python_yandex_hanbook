n = int(input())
m = int(input())
p1 = set([input() for _ in range(n)])
p2 = set([input() for _ in range(m)])

count = len(p1 & p2)
print(count if count > 0 else 'Таких нет')
