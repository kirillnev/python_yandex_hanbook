n = int(input())
m = int(input())
p = [input() for _ in range(n + m)]
p_set = set(p)

count = 0
for el in p_set:
    if p.count(el) == 1:
        count += 1
print(count if count > 0 else 'Таких нет')
