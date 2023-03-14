s = input()
n = [int(x) for x in s]
n.sort()
max_n = n[2] * 10 + n[1]
min_n = n[0] * 10 + n[1] if n[0] != 0 else n[1] * 10 + n[0]
print(min_n, max_n)
