from collections import Counter

n = int(input())
names = [input() for _ in range(n)]
names_dict = Counter(names)
namesakes = sum(list(filter(lambda x: x > 1, names_dict.values())))
print(namesakes)
