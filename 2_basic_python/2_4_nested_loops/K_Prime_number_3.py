def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
numbers = [int(input()) for i in range(n)]

prime_count = len(list(filter(is_prime, numbers)))
print(prime_count)
