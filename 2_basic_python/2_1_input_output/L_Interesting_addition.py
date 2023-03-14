n = int(input())
m = int(input())
res = (n // 100 + m // 100) % 10 * 100
res += (n % 100 // 10 + m % 100 // 10) % 10 * 10
res += (n % 10 + m % 10) % 10
print(res)
