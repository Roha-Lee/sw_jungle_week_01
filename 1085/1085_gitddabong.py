# x,y는 현재 나의 위치, w,h는 직사각형의 밑변과 높이의 길이
x, y, w, h = map(int, input().split())

# n의 위치가 0과 k중 어느 위치와 더 가까운지 출력
def whichClose(n, k):
    half = k/2
    # n의 길이가 변의 길이의 반값보다 크다? -> n은 k에 더 가깝다
    if n > half:
        return k
    # n의 길이가 변의 길이의 반값보다 작다? -> n은 0에 더 가깝다
    elif n < half: 
        return 0
    # 정확히 중간값인 경우 어느 값을 주든 상관없다
    else:
        return 0

# abs(n) : n의 절대값을 출력
min_x = abs(whichClose(x, w) - x)
min_y = abs(whichClose(y, h) - y)

print(min(min_x, min_y))