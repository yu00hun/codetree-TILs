arr = list(map(int, input().split()))
count_arr = [0] * 7

for elem in arr:
    count_arr[elem] += 1

for i in range(1, 7):
    print(f"{i} - {count_arr[i]}")