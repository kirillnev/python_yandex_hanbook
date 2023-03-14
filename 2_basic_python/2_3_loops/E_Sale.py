amount = 0
discount = 0.1
while (n := float(input())) != 0:
    amount += n if n < 500 else n * (1 - discount)

print(amount)
