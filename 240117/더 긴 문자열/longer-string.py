words = input().split()

len1 = len(words[0])
len2 = len(words[1])

if len1 > len2:
    print(words[0], len1)
else:
    print(words[1], len2)