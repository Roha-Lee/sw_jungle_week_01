import sys
input = sys.stdin.readline

location = 0
def zeta(n, r, c):
    global location
    if n == 0:
        return

    # 우선 좌표를 통해 찾고자하는 위치의 사분면을 찾기 (ㄷ순서/시계반대로 1234)
    # 1사분면
    if not(2 ** (n-1) > c) and 2 ** (n-1) > r:
        location += (2 ** (n-1)) ** 2
        zeta(n-1, r, c - 2 ** (n-1))

    # 3사분면
    elif 2 ** (n-1) > c and not(2 ** (n-1) > r):
        location += (2 ** (n-1)) ** 2 * 2
        zeta(n-1, r - 2 ** (n-1), c)
        
    # 4사분면
    elif not(2 ** (n-1) > c) and not(2 ** (n-1) > r):
        location += (2 ** (n-1)) ** 2 * 3
        zeta(n-1, r - 2 ** (n-1), c - 2 ** (n-1))
    # 2사분면
    else:
        zeta(n-1, r, c)
        
    
if __name__ == "__main__":
    n, r, c = map(int, input().split())
    zeta(n, r, c)
    print(location)
    