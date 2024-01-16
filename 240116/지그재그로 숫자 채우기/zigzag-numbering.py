n, m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

val = 0

for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            arr_2d[j][i] = val
            val += 1
        else:
            arr_2d[n-j-1][i] = val
            val += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()