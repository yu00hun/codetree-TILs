n = int(input())
arr = list(map(int, input().split()))
max_val = 0

for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[j] - arr[i] > max_val:
            max_val = arr[j] - arr[i]

print(max_val)