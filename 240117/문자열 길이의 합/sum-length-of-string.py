n = int(input())

total = 0
cnt = 0

for _ in range(n):
    word = input()
    total += len(word)
    if word[0] == 'a':
        cnt += 1

print(total, cnt)