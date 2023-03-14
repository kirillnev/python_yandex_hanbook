a = int(input())
b = int(input())

sign = 1 if b > a else -1
print(' '.join(map(str, range(a, b + sign, sign))))
