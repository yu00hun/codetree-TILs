first = input()
second = input()
str_first = ''
str_second = ''

for elem in first:
    if elem.isdigit():
        str_first += elem

for elem in second:
    if elem.isdigit():
        str_second += elem

print(int(str_first) + int(str_second))