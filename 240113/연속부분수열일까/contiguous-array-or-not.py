n1, n2 = tuple(map(int, input().split()))
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))
satisfied = False

for i in range(n1-n2+1):
    for j in range(i+n2):
        if B_arr == A_arr[i:j+1]:
            satisfied = True

if satisfied:
    print("Yes")
else:
    print("No")