n = int(input())
cnt = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    avg = sum(arr) / len(arr)

    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)