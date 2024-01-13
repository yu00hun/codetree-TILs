n = int(input())
arr = list(map(int, input().split()))
ans = 0
min_ans = 100

for i in range(n):
    for j in range(n):
        if i != j:
            if arr[i] > arr[j]:
                ans = arr[i] - arr[j]
                if ans < min_ans:
                    min_ans = ans
            else:
                ans = arr[j] - arr[i]
                if ans < min_ans:
                    min_ans = ans

print(min_ans)