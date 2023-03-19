from itertools import chain

lst = []
for _ in range(3):
    lst.append(input().split(', '))

sorted_lst = sorted(chain(*lst))
print(*[f'{i}. {s}' for i, s in enumerate(sorted_lst, 1)], sep='\n')
