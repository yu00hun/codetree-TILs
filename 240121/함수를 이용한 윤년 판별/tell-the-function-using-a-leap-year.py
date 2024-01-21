def leap_year(n):
    if n % 4 != 0:
        return False
    if n % 100 != 0:
        return True
    if n % 400 == 0:
        return True
    else:
        return False

year = int(input())

if leap_year(year):
    print('true')
else:
    print('false')