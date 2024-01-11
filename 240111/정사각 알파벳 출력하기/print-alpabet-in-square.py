n = int(input())
char = 'A'

for i in range(n):
    for j in range(n):
        print(char, end="")
        char = chr(ord(char) + 1)
    print()