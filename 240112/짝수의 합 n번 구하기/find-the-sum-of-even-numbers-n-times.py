n = int(input())

for i in range(n):
    a, b = tuple(map(int, input().split()))
    sum = 0

    for j in range(a, b+1):
        if j % 2 == 0:
            sum += j
        
    print(sum)