n = int(input())
arr = list(map(int, input().split()))
prev_max_idx = n

while True:
    max_idx = 0

    for i in range(1, prev_max_idx):
        if arr[i] > arr[max_idx]:
            max_idx = i
            
    print(max_idx + 1, end=" ")

    if max_idx == 0:
        break

    prev_max_idx = max_idx