from itertools import chain, permutations

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split(', '))

sorted_lst = sorted(chain(*lst))
print(*[f'{" ".join(v)}' for v in permutations(sorted_lst, 3)], sep='\n')
