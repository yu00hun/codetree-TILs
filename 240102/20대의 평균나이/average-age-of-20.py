sum = 0
cnt = 0

while True:
    age = int(input())

    if age >= 20 and age <= 29:
        sum += age
        cnt += 1
    else:
        print(f"{sum/cnt:.2f}")
        break