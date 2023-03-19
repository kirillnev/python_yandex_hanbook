import itertools
a, b, step = list(map(float, input().split()))
for x in itertools.count(a, step):
    if x >= b:
        break
    print(round(x, 2))
