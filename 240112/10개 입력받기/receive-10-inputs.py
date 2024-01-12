arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1
sum = sum(arr[:cnt])
avg = sum/cnt
print(f"{sum} {avg:.1f}")