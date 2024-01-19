arr = list(map(int, input().split()))

tmp = sum(arr)
cnt = 0

for elem in str(tmp):
    if elem == '1':
        cnt += 1
print(cnt)