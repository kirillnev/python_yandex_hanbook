str = input().split()
stack = []
for el in str:
    if el.isdigit():
        stack.append(int(el))
    else:
        b = stack.pop()
        a = stack.pop()
        if el == '+':
            stack.append(a + b)
        elif el == '-':
            stack.append(a - b)
        if el == '*':
            stack.append(a * b)
print(stack.pop())
