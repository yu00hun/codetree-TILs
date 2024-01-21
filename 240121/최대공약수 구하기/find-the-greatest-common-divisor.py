n, m = tuple(map(int, input().split()))

def gcd(n, m):
    result = 1
    for i in range(1, 101):
        if n % i == 0 and m % i == 0:
            result = i
    print(result)

gcd(n, m)