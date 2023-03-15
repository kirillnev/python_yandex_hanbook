numbers = list(map(int, input().split()))
power = int(input())
print(*[x**power for x in numbers], sep=' ')
