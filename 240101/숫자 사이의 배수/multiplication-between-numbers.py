input = input().split()
a, b = int(input[0]), int(input[1])
sum = 0
cnt = 0
avg = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        cnt += 1
        avg = sum / cnt

print(f"{sum} {avg:.1f}")