n = int(input())
tmp = 0

for _ in range(n):
    num = int(input())
    tmp += num

str_tmp = str(tmp)

result = str_tmp[1:] + str_tmp[0]
print(result)