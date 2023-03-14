s = [input(), input(), input()]

s.sort()

for el in s:
    if 'зайка' in el:
        print(el, len(el))
        break
