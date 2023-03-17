n_dishes = int(input())
dishes = set(input() for _ in range(n_dishes))

n_days = int(input())
dishes_per_day = []
for i in range(n_days):
    n = int(input())
    dishes_per_day.append([input() for _ in range(n)])

res = list(dishes - set(sum(dishes_per_day, [])))
if res:
    res.sort()
    print(*res, sep='\n')
else:
    print('Готовить нечего')
