arr = list(map(int, input().split()))
idx = 0

for elem in arr:

    if elem == 999 or elem == -999:
        break

    idx += 1

print(max(arr[0:idx]), min(arr[0:idx]))