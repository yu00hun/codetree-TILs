while True:
    inp = input().split()
    
    a, b, c = int(inp[0]), int(inp[1]), inp[2]

    print(a * b)

    if c == 'C':
        break