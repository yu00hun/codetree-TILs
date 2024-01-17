word = input()
tmp = input()
cnt = 0

for i in range(len(word)):
    if word[i] == tmp:
        cnt += 1

print(cnt)