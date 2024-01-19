a, b, c = tuple(map(int, input().split()))
satisfied = False

for i in range(a, b+1):
    if i % c == 0:
        satisfied = True

if satisfied:
    print("NO")
else:
    print("YES")