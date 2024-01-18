a = input()
b = input()

len_a = len(a)
len_b = len(b)

cnt = 0

for i in range(len_a - len_b + 1):
    is_matched = True
    for j in range(len_b):
        if a[i+j] != b[j]:
            is_matched = False
    
    if is_matched:
        cnt += 1

print(cnt)