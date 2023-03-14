n = int(input())
max_sum = 0
max_name = ''
for i in range(n):
    cur_name = input()
    cur_sum = sum(map(int, list(input())))
    if cur_sum >= max_sum:
        max_sum = cur_sum
        max_name = cur_name

print(max_name)
