A = input()
B = input()
len_A = len(A)
cnt = -1

for _ in range(len_A):
    if A == B:
        break
    A = A[-1] + A[:-1]
    cnt += 1

if cnt == len_A:
    print(-1)
else:
    print(cnt+1)