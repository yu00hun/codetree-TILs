string = input()

pos = string.find('e')

string = string[:pos] + string[pos+1:]

print(string)