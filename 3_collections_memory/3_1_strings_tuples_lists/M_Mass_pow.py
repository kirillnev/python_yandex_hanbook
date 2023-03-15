n = int(input())
numbers = [int(input()) for _ in range(n)]
pow_value = int(input())

print(*[x**pow_value for x in numbers], sep='\n')