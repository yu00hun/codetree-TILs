N = int(input())
arr = []
max_cnt = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(N):
    for j in range(N-2):
        cnt = 0
        if arr[i][j] == 1:
            cnt +=1
        if arr[i][j+1] == 1:
            cnt +=1
        if arr[i][j+2] == 1:
            cnt +=1

        max_cnt = max(max_cnt, cnt)


print(max_cnt)