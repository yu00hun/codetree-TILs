string = input()
arr = list(string)

arr.pop(1)
arr.pop(-2)

answer = ''.join(arr)
print(answer)