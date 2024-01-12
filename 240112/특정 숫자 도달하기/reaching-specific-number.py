arr = list(map(int,input().split()))
ans = []
sum = 0

for elem in arr:
    if elem < 250:
        ans.append(elem)
    else:
        break
        
for elem in ans:
    sum += elem

print(f"{sum} {sum/len(ans):.1f}")