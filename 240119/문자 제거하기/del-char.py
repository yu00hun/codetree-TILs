string = input()
arr = list(string)
leng = len(string)

for _ in range(leng):
    n = int(input())
    
    if n > len(arr):
        arr.pop(-1)
    else:
        arr.pop(n)

    answer = ''.join(arr)
    print(answer)

    if len(arr) == 1:
        break