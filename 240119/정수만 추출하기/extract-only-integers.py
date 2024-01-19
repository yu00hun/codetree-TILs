arr = list(input().split())
string = ''
result = 0

for elem in arr:
    for item in elem:
        if item.isdigit():
            string += item
        else:
            break
    result += int(string)
    string = ''

print(result)