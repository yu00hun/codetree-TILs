n = int(input())
ans = []
cnt = 0

for i in range(1, 20):
    ans.append(n*i)

    if n*i % 5 == 0:
        cnt += 1

    if cnt == 2:
        break

for elem in ans:
    print(elem, end=" ")