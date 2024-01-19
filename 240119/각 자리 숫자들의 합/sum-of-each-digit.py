n = int(input())
str_n = str(n)
result = 0

for elem in str_n:
    result += int(elem)

print(result)