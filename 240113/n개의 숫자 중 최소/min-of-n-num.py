n = int(input())
arr = list(map(int, input().split()))
min_num = arr[0]

for elem in arr:
    if min_num > elem:
        min_num = elem

print(min_num, arr.count(min_num))