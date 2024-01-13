n = int(input())
ans = [1, n]

while True:
    ans.append(ans[-1]+ans[-2])
    if ans[-1] > 100:
        break

for elem in ans:
    print(elem, end=" ")