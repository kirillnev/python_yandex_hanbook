loc_objects = []
while (location := input()) != '':
    loc_objects.append(location.split())

neighbours = set()
for loc in loc_objects:
    for i in range(len(loc)):
        if loc[i] == 'зайка':
            if i == 0 and len(loc) > 1:
                neighbours.add(loc[1])
            elif i == len(loc) - 1:
                neighbours.add(loc[i - 1])
            else:
                neighbours.add(loc[i - 1])
                neighbours.add(loc[i + 1])

res = list(neighbours)
res.sort()
print(*res, sep='\n')

t = '''
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка
'''