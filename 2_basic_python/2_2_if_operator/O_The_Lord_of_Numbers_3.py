num1 = input()
num2 = input()
digits = list(map(int, list(num1 + num2)))
digits.sort()
res = digits[3] * 100 + (digits[2] + digits[1]) % 10 * 10 + digits[0]
print(res)
