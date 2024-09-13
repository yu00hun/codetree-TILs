a, o, c = map(str, input().split())
a, c = int(a), int(c)

# 덧셈
def plus(a, c):
    return a + c

# 뺄셈
def minus(a, c):
    return a - c

# 곱셈
def mul(a, c):
    return a * c

# 나눗셈
def div(a, c):
    return a // c

if o == '+':
    print(a, o, c, '=', a, o, c, '=', plus(a, c))
elif o == '-':
    print(a, o, c, '=', minus(a, c))
elif o == '*':
    print(a, o, c, '=', mul(a, c))
elif o == '/':
    print(a, o, c, '=', div(a, c))
else:
    print('False')