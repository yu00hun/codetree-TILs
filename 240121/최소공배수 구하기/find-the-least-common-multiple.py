n, m = tuple(map(int, input().split()))

def lcm(n, m):
    result = 0
    for i in range(1, min(n,m)+1):
        if n % i == 0 and m % i == 0:
            result = i

    print(n * m // result)

lcm(n, m)