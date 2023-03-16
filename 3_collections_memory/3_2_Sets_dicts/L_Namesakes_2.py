from collections import Counter

n = int(input())
names = [input() for _ in range(n)]
names_dict = Counter(names)
namesakes = dict(filter(lambda x: x[1] > 1, names_dict.items()))
namesakes = dict(sorted(namesakes.items(), key=lambda x: x[0]))
if len(namesakes) > 0:
    for name, count in namesakes.items():
        print(name, '-', count)
else:
    print('Однофамильцев нет')
