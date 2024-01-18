string = input()
arr = list(string)

first = string[0]
second = string[1]

for i in range(len(arr)):
    if arr[i] == first:
        arr[i] = second
    elif arr[i] == second:
        arr[i] = first

answer = ''.join(arr)
print(answer)