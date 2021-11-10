import sys 

def find_order(N, r, c):
    if N == 0:
        return 0

    # 44일때
    r_ = r // 2 # -> 1  
    c_ = c // 2 # -> 0
    square = 2 ** (N-1) * 2 ** (N-1) 
    # 6일때  -> r_ : 0, c_ : 0 -> 사각형 0개 더해줘야함
    # 22일때 -> r_ : 0, c_ : 1 -> 사각형 1개 더해줘야함
    # 44일때 -> r_ : 1, c_ : 0 -> 사각형 2개 더해줘야함 
    # 61일때 -> r_ : 1, c_ : 1 -> 사각형 3개 더해줘야함
    new_r = r % (2 ** (N-1))
    new_c = c % (2 ** (N-1))
    #       4*4일때 위치            +  2*2일떄의 위치                   + 1*1일때의 위치                +  0
    return square * (2 * r_ + c_) + find_order(N-1, new_r, new_c)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, r, c = map(int, input().split())
