input = input().split()
a, b = int(input[0]), int(input[1])
prod = 1

for i in range(a, b+1):
    prod *= i

print(prod)