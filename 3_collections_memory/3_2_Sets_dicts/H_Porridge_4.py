n = int(input())
children = {}
for el in [input() for _ in range(n)]:
    child = el.split()
    children[child[0]] = child[1:]
porridge = input()

children_like_porridge = dict(filter(lambda x: porridge in x[1], children.items()))
if len(children_like_porridge) > 0:
    print(*sorted(children_like_porridge.keys()), sep='\n')
else:
    print('Таких нет')
