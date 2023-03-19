from itertools import permutations

n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

lst.sort()
print(*[', '.join(v) for v in permutations(lst)], sep='\n')
