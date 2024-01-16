arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    sum_row = 0
    for j in range(4):
        sum_row += arr_2d[i][j]
    print(f"{sum_row / 4:.1f}", end=" ")

print()

for i in range(4):
    sum_col = 0
    for j in range(2):
        sum_col += arr_2d[j][i]
    print(f"{sum_col / 2:.1f}", end=" ")

print()

sum_total = 0

for i in range(2):
    for j in range(4):
        sum_total += arr_2d[i][j]
print(f"{sum_total / 8:.1f}")