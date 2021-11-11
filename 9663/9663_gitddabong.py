import sys

def queen(depth = 0):
    global count

    # 모든 경로를 거쳐왔다면 퀸을 다 놓았다는 것이므로 카운트 1 추가
    if depth == n:
        count += 1
        return

    # 열을 옮겨다니며 놓을 수 있는 곳을 탐색
    # 대각선 / 성분은 총 2**n-1 개인데, 각 행과 열의 숫자의 합으로 모두 표현 가능하다.
    # 대각선 \ 성분은 각 행과 열의 숫자의 차 +(n-1)로 모두 표현 가능하다.
    for i in range(n):
        if put_row[i] == False and put_slash[depth + i] == False and put_r_slash[depth - i + (n-1)] == False:
            put_row[i] = True
            put_slash[depth + i] = True
            put_r_slash[depth - i + (n-1)] = True
            queen(depth + 1)
            put_row[i] = False
            put_slash[depth + i] = False
            put_r_slash[depth - i + (n-1)] = False

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())

    put_row = [False] * n
    put_slash = [False] * (2**n - 1)
    put_r_slash = [False] * (2**n - 1)
    
    count = 0
    queen()
    print(count)