from collections import Counter

strs = ''
while (s := input()) != 'ФИНИШ':
    strs += s
print(Counter(sorted(list(strs.lower().replace(' ', '')))).most_common(1)[0][0])