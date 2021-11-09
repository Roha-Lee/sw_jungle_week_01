import sys 
count = 0 
def hanoi(n, src=1, dst=3): 
    global count
    if n > 1:
        hanoi(n-1, src, 6-src-dst)
    
    print(src, dst)
    count = count + 1
    if n > 1:
        hanoi(n-1, 6-src-dst, dst)

# def print_my_num(my_num = 7):
#     print(my_num)
# print_my_num(8)
# print_my_num()

# 지역변수 & 전역변수 

# my_num = 7
# def print_my_num():
#     print(my_num)


# def modify_my_num():
#     global my_num
#     my_num += 7

# modify_my_num()
# .
# .
# 1000줄
# .
# .
# print_my_num()

# 탐색 
# for i in [1,2,3,4,5]:
#     print(i)

'''
hanoi(5)
if n > 1:
    hanoi(4, 1, 2)
    if n > 1:
        hanoi(3, 1, 3)
        if n > 1:
            hanoi(2, 1, 2)
            if n > 1:
                hanoi(1, 1, 3)
                    print(1, 3)
                종료 
            print(1, 2)
            if n > 1:
                hanoi(1, 2, 3)
                    print(2, 3)
                종료 
            종료
        print(1, 3)
        if n > 1:
            hanoi(2, 3, 2)
    
종료
'''

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(2**n - 1)
    hanoi(n)
