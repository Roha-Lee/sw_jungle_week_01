n, x = map(int, input().split())
array = list(map(int, input().split()))

for num in array:
    if x > num:
        print(num, end=" ")
    else:
        continue