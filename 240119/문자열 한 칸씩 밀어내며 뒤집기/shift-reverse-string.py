string, q = tuple(input().split())
q = int(q)

for _ in range(q):
    request = int(input())

    if request == 1:
        string = string[1:] + string[0]
    elif request == 2:
        string = string[-1] + string[:-1]
    elif request == 3:
        string = string[::-1]

    print(string)