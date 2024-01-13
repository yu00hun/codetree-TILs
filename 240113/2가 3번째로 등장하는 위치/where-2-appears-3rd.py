n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i, elem in enumerate(arr):
    if elem == 2:
        cnt += 1

    if cnt == 3:
        print(i+1)
        break