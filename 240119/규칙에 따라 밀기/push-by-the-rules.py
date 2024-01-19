string = input()
rule = input()

for elem in rule:
    if elem == "L":
        string = string[1:] + string[0]
    elif elem == "R":
        string = string[-1] + string[:-1]
    
print(string)