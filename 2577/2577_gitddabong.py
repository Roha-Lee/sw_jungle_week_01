result = 1
for i in range(3):
    result *= int(input())

str_result = list(str(result))
num_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(str_result)):
    num_list[int(str_result[i])] += 1

for num in num_list:
    print(num)