string = input()
target = input()

# print(string.find(target))

for i in range(len(string)-len(target)+1):
    is_matched = True
    for j in range(len(target)):
        if string[i+j] != target[j]:
            is_matched = False

    if is_matched:
        print(i)
        break

if is_matched == False:
    print(-1)