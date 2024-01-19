arr = list(input().split('.'))

for elem in arr:
    if elem.isalpha():
        print(elem.upper(), end="")