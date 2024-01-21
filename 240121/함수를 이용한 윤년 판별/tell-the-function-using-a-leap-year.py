def leap_year(n):
    if n % 4 != 0:
        return False
    if n % 4 == 0 and n % 100 == 0:
        return False
    if n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        return False
    else:
        return True

year = int(input())

if leap_year(year):
    print('true')
else:
    print('false')