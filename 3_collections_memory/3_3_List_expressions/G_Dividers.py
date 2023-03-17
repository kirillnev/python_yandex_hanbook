numbers = {15, 49, 36}
print({n: [d for d in range(1, n + 1) if n % d == 0] for n in numbers})