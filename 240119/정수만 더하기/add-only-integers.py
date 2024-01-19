A = input()
result = 0

for elem in A:
    if elem.isdigit():
        result += int(elem)
        
print(result)