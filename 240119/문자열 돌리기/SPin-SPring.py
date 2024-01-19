string = input()
leng = len(string)

for _ in range(leng+1):
    print(string)
    string = string[-1] + string[:-1]