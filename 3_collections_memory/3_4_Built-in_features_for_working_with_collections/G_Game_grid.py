from itertools import combinations
n = int(input())
lst = [input() for _ in range(n)]

for v1, v2 in combinations(lst, 2):
    print(v1, '-', v2)