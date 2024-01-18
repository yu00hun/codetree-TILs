first, second = tuple(input().split())

arr_first = list(first)
arr_second = list(second)

arr = arr_first[:2] + arr_second[2:]
answer = ''.join(arr)

print(answer)