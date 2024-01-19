string_a = input()
string_b = input()
len_a = len(string_a)
len_b = len(string_b)

while True:
    idx = -1
    for i in range(len_a - len_b + 1):
        exist = True
        for j in range(len_b):
            if string_a[i+j] != string_b[j]:
                exist = False
                break
        
        if exist:
            idx = i
            break

    if idx == -1:
        break
    
    string_a = string_a[:idx] + string_a[idx + len_b:]

    len_a = len(string_a)

print(string_a)