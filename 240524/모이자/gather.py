n = int(input())
house = list(map(int, input().split()))
distance = []

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += house[j] * abs(j-i)

    distance.append(tmp)

print(min(distance))