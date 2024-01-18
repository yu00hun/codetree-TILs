string = input()

list = []
cnt = 1

for i in range(len(string)-1):

    if string[i] == string[i+1]:
        cnt += 1
        if i == len(string) - 2:
            list.append(f"{string[i]}{cnt}")
        
    else:
        list.append(f"{string[i]}{cnt}")
        cnt = 1

leng = 0
for i in range(len(list)):
    leng += len(list[i])
print(leng)

for elem in list:
    print(elem, end="")