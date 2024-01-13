a, b = tuple(map(int, input().split()))
count_arr = [0] * 10
ans = 0

for i in range(100):
    count_arr[a%b] += 1
    a = a // b
    
    if a <= 1:
        break
        
for elem in count_arr:
    ans += elem * elem

print(ans)