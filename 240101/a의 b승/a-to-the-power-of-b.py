input = input().split()
a, b = int(input[0]), int(input[1])
prod = 1

for _ in range(b):
    prod *= a

print(prod)