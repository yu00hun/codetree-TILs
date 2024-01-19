string = input()

for elem in string:
    if (ord(elem) >= ord('a') and ord(elem) <= ord('z')):
        elem = chr(ord(elem) - ord('a') + ord('A'))

    elif (ord(elem) >= ord('A') and ord(elem) <= ord('Z')):
        elem = chr(ord(elem) - ord('A') + ord('a'))

    print(elem, end="")