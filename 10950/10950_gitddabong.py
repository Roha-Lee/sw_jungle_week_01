n = int(input())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))
    
for num in array:
    print(num[0] + num[1])