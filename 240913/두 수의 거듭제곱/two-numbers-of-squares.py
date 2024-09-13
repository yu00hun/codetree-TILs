a, b = map(int, input().split())

# ans = a ** b
def power(a, b):
    res = 1
    for _ in range(b):
        res *= a

    return res

print(power(a, b))