n = int(input())

for i in range(n):
    inp = input().split()
    a, b = int(inp[0]), int(inp[1])
    prod = 1
    for j in range(a, b+1):
        prod *= j
    print(prod)