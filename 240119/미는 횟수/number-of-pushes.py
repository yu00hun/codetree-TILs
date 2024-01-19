A = input()
B = input()
len_A = len(A)
cnt = 0

for i in range(len_A):
    A = A[-1] + A[:-1]
    cnt += 1
    if A == B:
        break

if cnt == 0:
    print(-1)
else:
    print(cnt)