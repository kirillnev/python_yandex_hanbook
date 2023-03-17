def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


nums = list(set(map(int, input().split('; '))))
nums.sort()
n = len(nums)

res = {}
for i in range(n):
    res[nums[i]] = []
    for j in range(n):
        if i != j and nums[i] != nums[j] and gcd(nums[i], nums[j]) == 1:
            res[nums[i]].append(str(nums[j]))

for num, simples in res.items():
    if simples:
        print(f'{num} - {", ".join(simples)}')
