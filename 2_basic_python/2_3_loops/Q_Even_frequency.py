n = list(map(int, input()))
print(*list(filter(lambda x: x % 2 != 0, n)), sep='')