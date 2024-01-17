arr = [
    input()
    for _ in range(10)
]

word = input()
result = False

for i in range(10):
    if arr[i][-1] == word:
        print(arr[i])
        result = True
    
if result == False:
    print('None')