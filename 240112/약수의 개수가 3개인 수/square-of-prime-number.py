start, end = tuple(map(int, input().split()))
result = 0

for i in range(start, end+1):
    cnt = 0
    for j in range(1, i+1):
        if start % i == 0:
            cnt += 1
    if cnt == 3:
        result += 1

print(result)