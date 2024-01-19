string = input()
arr = list(string)
leng = len(arr)

for _ in range(leng):
    n = int(input())
    
    if n > len(arr) - 1:
        arr.pop(-1)
    else:
        arr.pop(n)

    answer = ''.join(arr)
    print(answer)

    if len(arr) == 1:
        break