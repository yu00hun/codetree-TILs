m = int(input())

for i in range(m):
    num = int(input())
    cnt = 0
    while(num != 1):
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1

        cnt += 1
    
    print(cnt)