def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)


a = int(input())
b = int(input())
print(nod(a, b))
