cnt = 0
answer = []
while True:
    string = input()

    if string == '0':
        break

    if cnt % 2 == 0:
        answer.append(string)

    cnt += 1

print(cnt)

for elem in answer:
    print(elem)