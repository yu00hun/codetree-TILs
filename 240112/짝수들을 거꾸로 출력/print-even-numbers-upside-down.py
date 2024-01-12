n = int(input())
arr = list(map(int, input().split()))
ans = []

for elem in arr:
    if elem % 2 == 0:
        ans.append(elem)

for i in ans[::-1]:
    print(i, end=" ")