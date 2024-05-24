N = int(input())
cattle = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cattle[i] <= cattle[j] <= cattle[k]:
                cnt += 1

print(cnt)