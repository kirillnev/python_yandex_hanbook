from collections import Counter
loc_objects = []
while (location := input()) != '':
    loc_objects += location.split()

counter_objects = dict(Counter(loc_objects))
print(*[f'{el[0]} {el[1]}' for el in counter_objects.items()], sep='\n')
