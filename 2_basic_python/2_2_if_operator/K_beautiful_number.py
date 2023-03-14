s = list(map(int, list(input())))
s.sort()
print('YES' if s[0] + s[2] == s[1] * 2 else 'NO')
