n = int(input())
num = 0

for i in range(n):
    for j in range(1, n+1):
        if i % 2 == 0:
            num += 1
            print(num, end=" ")
        else:
            num += 2
            print(num, end=" ")
    print()