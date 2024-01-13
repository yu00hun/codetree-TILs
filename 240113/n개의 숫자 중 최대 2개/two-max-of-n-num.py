n = int(input())
arr = list(map(int, input().split()))
max_val = arr[0]

for i in range(n):
    for j in range(n):
        if arr[i] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp

print(arr[0], arr[1])