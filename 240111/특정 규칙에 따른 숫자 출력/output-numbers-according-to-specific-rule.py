n = int(input())
num = 1

for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for j in range(n-i):
        print(num, end=" ")
        num += 1
        
    if num == 10:
        num = 1

    print()