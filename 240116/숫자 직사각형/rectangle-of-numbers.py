n, m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

val = 1

for i in range(n):
    for j in range(m):
        arr_2d[i][j] += val
        val += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()