n = int(input())
print('А Б В')
for i in range(1, n):
    for j in range(1, n - i):
        k = n - i - j

        if i >= 1 and j >= 1 and k >= 1:
            print(i, j, k)
