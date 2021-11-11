array = []
for i in range(9):
    array.append(int(input()))

maximum = 0
index = 0

for i in range(9):
    if array[i] > maximum:
        maximum = array[i]
        index = i

print(maximum)
print(index + 1) # 인덱스는 0이지만 몇 번째 수인지 출력하는게 정답이므로 +1