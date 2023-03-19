lst1 = input().split(', ')
lst2 = input().split(', ')
for name1, name2 in zip(lst1, lst2):
    print(f'{name1} - {name2}')