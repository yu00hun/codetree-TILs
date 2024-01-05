inp = input().split()
a, b = int(inp[0]), int(inp[1])
satisfied = False

for i in range(a, b+1):
    if 1920 % i == 0 or 2880 % i == 0:
        satisfied = True

if satisfied:
    print(1)
else:
    print(0)