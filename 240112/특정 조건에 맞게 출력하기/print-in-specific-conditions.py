arr = list(map(int, input().split()))
ans = []

for elem in arr:
    if elem == 0:
        break
    if elem % 2 != 0:
        ans.append(elem + 3)
    else:
        ans.append(elem // 2)

for elem in ans:
    print(elem, end=" ")