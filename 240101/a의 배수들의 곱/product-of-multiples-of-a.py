input = input().split()
a, b = int(input[0]), int(input[1])
prod = 1

for i in range(1, b+1):
    if i % a == 0:
        prod *= i

print(prod)