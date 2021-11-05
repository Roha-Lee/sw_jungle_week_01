a = int (input())

# for i in range(a):
#     if i == 0:
#         print('*')
#     else:   
#         i = '*' + '*' * int(i)
#         print(i)

for i in range(1, a+1):
    star = "*" * i
    print(star)