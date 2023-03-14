n = int(input())
s = 0
for i in range(n):
    s += sum(map(int, list(input())))

print(s)
