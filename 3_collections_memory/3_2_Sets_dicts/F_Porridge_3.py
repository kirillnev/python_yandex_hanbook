from collections import Counter
n = int(input())
m = int(input())
p = [input() for _ in range(n + m)]

p_count = list(filter(lambda x: x[1] == 1, Counter(p).items()))
if len(p_count) > 0:
    res = [x[0] for x in p_count]
    res.sort()
    print(*res, sep='\n')
else:
    print('Таких нет')