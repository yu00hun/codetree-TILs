count_arr = [0] * 4

for _ in range(3):
    arr = list(input().split())

    if arr[0] == 'Y' and int(arr[1]) >= 37:
        count_arr[0] += 1
    elif arr[0] == 'N' and int(arr[1]) >= 37:
        count_arr[1] += 1
    elif arr[0] == 'Y' and int(arr[1]) < 37:
        count_arr[2] += 1
    else:
        count_arr[3] += 1
    
for elem in count_arr:
    print(elem, end=" ")
    
if count_arr[0] >= 2:
    print('E')