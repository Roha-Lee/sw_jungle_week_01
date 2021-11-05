num = []
for i in range(1, 10):
    i = int(input())
    num.append(i)

print(max(num))
print(num.index(max(num))+1)