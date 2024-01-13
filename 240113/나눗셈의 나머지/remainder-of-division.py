a, b = tuple(map(int, input().split()))
count_arr = [0] * 10
ans = 0

while a > 1:
    count_arr[a%b] += 1
    a = a // b


for elem in count_arr:
    ans += elem * elem

print(ans)