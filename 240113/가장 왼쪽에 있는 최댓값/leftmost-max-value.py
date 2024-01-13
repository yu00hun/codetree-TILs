n = int(input())
arr = list(map(int, input().split()))
max_val = 0
idx = 0

while True:
    max_val = max(arr)
    idx = arr.index(max_val)
    print(idx+1, end=" ")
    arr = arr[:idx]

    if idx == 0:
        break