n = int(input())
char = 'A'

for i in range(n):
    for j in range(i+1):
        if char == 'Z':
            char = 'A'
        print(char, end="")
        char = chr(ord(char)+1)
    print()