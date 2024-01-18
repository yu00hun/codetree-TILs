string = input()
tmp = list(string)
first = string[0]
second = string[1]

for i in range(len(string)):
    if tmp[i] == second:
        tmp[i] = first
        
answer = ''.join(tmp)
print(answer)