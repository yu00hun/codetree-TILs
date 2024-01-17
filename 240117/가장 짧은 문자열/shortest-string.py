arr = []

for _ in range(3):
    word = input()
    arr.append(len(word))

print(max(arr) - min(arr))