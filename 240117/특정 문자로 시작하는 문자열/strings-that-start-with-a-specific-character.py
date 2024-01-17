n = int(input())
arr = [
    input()
    for _ in range(n)
]
word = input()
cnt = 0
total_len = 0

for i in range(4):
    if arr[i][0] == word:
        cnt += 1
        total_len += len(arr[i])

print(f"{cnt} {total_len/cnt:.2f}")