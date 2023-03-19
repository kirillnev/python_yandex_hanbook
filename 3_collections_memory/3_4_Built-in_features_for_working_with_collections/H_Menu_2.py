from itertools import cycle, islice
n = int(input())
lst = [input() for _ in range(n)]
days = int(input())

for val in islice(cycle(lst), 0, days, 1):
    print(val)

