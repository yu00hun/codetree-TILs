string = input()
n = int(input())

length = len(string)

for i in range(n):
    print(string[length-i-1], end="")