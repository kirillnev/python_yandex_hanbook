def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result


n = int(input())
print(gcd_list([int(input()) for i in range(n)]))
