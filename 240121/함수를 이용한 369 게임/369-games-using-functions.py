def is_369(i):
    i = str(i)
    for elem in i:
        if elem == '3' or elem == '6' or elem == '9':
            return True


def is_magic_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 3 == 0 or is_369(i):
            cnt += 1
    return cnt


a, b = tuple(map(int, input().split()))

print(is_magic_number(a, b))