string = input()
n = int(input())

for elem in string[-1:-n-1:-1]:
    print(elem, end="")