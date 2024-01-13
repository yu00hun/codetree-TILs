arr = list(map(int, input().split()))
max_num = arr[0]

for elem in arr:
    if elem >= max_num:
        max_num = elem

print(max_num)