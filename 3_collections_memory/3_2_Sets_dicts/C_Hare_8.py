n = int(input())
my_set = set()
for _ in range(n):
    my_set = my_set | set(input().split())

print(*my_set, sep='\n')
