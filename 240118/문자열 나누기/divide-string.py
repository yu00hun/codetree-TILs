n = int(input())
arr = list(input().split())
temp = ""

for elem in arr:
    temp += elem

cnt = 0
for elem in temp:
    print(elem, end="")
    cnt += 1
    if cnt == 5:
        cnt = 0
        print()