arr = ["apple", "banana", "grape", "blueberry", "orange"]

word = input()
cnt = 0

for item in arr:
    if item[2] == word or item[3] == word:
        print(item)
        cnt += 1
print(cnt)