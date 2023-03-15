import math

str = input().split()
stack = []
unary = ('~', '!', '#', )
binary = ('+', '-', '*', '/')
ternary = ('@')
for el in str:
    if el.isdigit():
        stack.append(int(el))
    else:
        if el in unary:
            a = stack.pop()
            if el == '~':
                stack.append(-a)
            elif el == '!':
                stack.append(math.factorial(a))
            elif el == '#':
                stack.append(a)
                stack.append(a)
        if el in binary:
            b = stack.pop()
            a = stack.pop()
            if el == '+':
                stack.append(a + b)
            elif el == '-':
                stack.append(a - b)
            elif el == '*':
                stack.append(a * b)
            elif el == '/':
                stack.append(a // b)
        elif el in ternary:
            c = stack.pop()
            b = stack.pop()
            a = stack.pop()
            stack.append(b)
            stack.append(c)
            stack.append(a)

print(stack.pop())
