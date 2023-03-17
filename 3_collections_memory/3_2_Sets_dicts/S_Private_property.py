from collections import Counter
n = int(input())
toys = []
for _ in range(n):
    toys += list(set(input().split(': ')[1].split(', ')))
unique_toys = dict(filter(lambda x: x[1] == 1, Counter(toys).items()))
print(*sorted(unique_toys.keys()), sep='\n')
