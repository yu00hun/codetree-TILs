n, q = tuple(map(int, input().split()))
n_arr = list(map(int, input().split()))

for i in range(q):
    q_arr = list(map(int, input().split()))

    if q_arr[0] == 1:
        print(n_arr[q_arr[1]-1])
    elif q_arr[0] == 2:
        if q_arr[1] in n_arr:
            print(n_arr.index(q_arr[1])+1)
        else:
            print(0)
    elif q_arr[0] == 3:
        for i in range(q_arr[1], q_arr[2]+1):
            print(n_arr[i-1], end=" ")

1 24
2 85
2 98
59
31
0