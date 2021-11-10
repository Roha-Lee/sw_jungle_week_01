a = int(input())

# (4의 배수이면서and 100의 배수가 아님) or (400의 배수이면)
if (a % 4 == 0 and (a % 100 != 0)) or (a % 400 == 0):
    print('1')
else : 
    print('0')