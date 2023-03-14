n = int(input())
s = [input() for i in range(n)]
count = len(list(filter(lambda x: 'зайка' in x, s)))

print(count)
