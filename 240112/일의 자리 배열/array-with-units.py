arr = list(map(int, input().split()))

for _ in range(8):
    tmp = arr[-1] + arr[-2]
    arr.append(tmp%10)

for elem in arr:
    print(elem, end=" ")