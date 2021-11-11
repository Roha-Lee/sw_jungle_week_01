n = int(input())

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
def isYoon(n):
    if (n % 4 == 0 and not(n % 100 == 0)) or (n % 400 == 0):
        return 1
    else:
        return 0

print(isYoon(n))