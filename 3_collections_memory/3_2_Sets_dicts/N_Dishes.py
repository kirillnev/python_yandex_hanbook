n_items = int(input())
items = set(input() for _ in range(n_items))

n_dishes = int(input())
dishes = {}
for i in range(n_dishes):
    name = input()
    n = int(input())
    dishes[name] = [input() for _ in range(n)]

can_cook = []
for k, v in dishes.items():
    if set(v).issubset(items):
        can_cook.append(k)
if can_cook:
    can_cook.sort()
    print(*can_cook, sep='\n')
else:
    print('Готовить нечего')
