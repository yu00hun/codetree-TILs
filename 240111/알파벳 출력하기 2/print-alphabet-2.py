n = int(input())
char = "A"

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n-i):
        print(char, end=" ")
        char = chr(ord(char)+1)
    print()