s = list(map(int, list(input())))
p = [s[2] + s[1], s[0] + s[1]]
p.sort(reverse=True)
print(str(p[0]) + str(p[1]))
