from itertools import chain

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split(', '))

sorted_lst = sorted(chain(*lst))
print(*[f'{i}. {s}' for i, s in enumerate(sorted_lst, 1)], sep='\n')
