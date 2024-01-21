n = int(input())

def calculate(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum // 10

result = calculate(n)
print(result)