nums = list(map(int, input().split()))

binary_nums = [bin(num)[2:] for num in nums]

res = []
for num in binary_nums:
    n_lst = list(str(num))
    res.append({'digits': len(n_lst), 'units': n_lst.count('1'), 'zeros': n_lst.count('0')})

print(res)
