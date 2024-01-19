char = input()
if char == 'a':
    print('z')
else:
    answer = chr(ord(char) - 1)
    print(answer)