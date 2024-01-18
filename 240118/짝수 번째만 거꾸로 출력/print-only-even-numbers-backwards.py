string = input()

answer = ""

for i in range(len(string)):
    if i % 2 == 1:
        answer += string[i]

for i in range(len(answer)):
    print(answer[len(answer)-i-1], end="")