s, q = tuple(input().split())
arr = list(s)
q = int(q)

for i in range(q):
    n, a, b = tuple(input().split())
    n = int(n)

    if n == 1:
        a, b = int(a), int(b)
        tmp = arr[a-1]
        arr[a-1] = arr[b-1]
        arr[b-1] = tmp

    elif n == 2:
        for j in range(len(s)):
            if arr[j] == a:
                arr[j] = b

    answer = ''.join(arr)
    print(answer)