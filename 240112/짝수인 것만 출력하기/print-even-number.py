n = int(input())
arr = list(map(int, input().split()))
ans = []

for elem in arr:
    if elem % 2 == 0:
        ans.append(elem)
    
for elem in ans:
    print(elem, end=" ")