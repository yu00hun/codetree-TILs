n = int(input())
satisfied = False

for i in range(2, n+1):
    if n % i == 0:
        satisfied = True
        break

if satisfied:
    print("C")
else:
    print("N")