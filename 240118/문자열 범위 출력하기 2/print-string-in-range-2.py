string = input()
n = int(input())

length = len(string)

for i in range(11):
    print(string[length-i-1], end="")