v = {}
v['Петя'] = int(input())
v['Вася'] = int(input())
v['Толя'] = int(input())

v = dict(sorted(v.items(), key=lambda x: x[1], reverse=True))
for i, el in enumerate(v.keys()):
    print(f'{i + 1}. {el}')
