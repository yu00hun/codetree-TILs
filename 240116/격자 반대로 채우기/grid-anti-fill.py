n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

count = 1

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if n % 2 == 0:
            if i % 2 == 0:
                arr_2d[n-j-1][i] = count
            else:
                arr_2d[j][i] = count
        else:
            if i % 2 == 0:
                arr_2d[j][i] = count
            else:
                arr_2d[n-j-1][i] = count
        count += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()