a1, a2 = tuple(map(int, input().split()))
ans = [a1, a2]

for i in range(2, 10):
    ans.append(ans[i-1] + 2*ans[i-2])

for elem in ans:
    print(elem, end=" ")