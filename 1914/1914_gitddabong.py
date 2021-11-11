import sys
input = sys.stdin.readline

# 원반 n개를 x기둥에서 y기둥으로 옮기기
def hanoi(n, x, y):
    if n == 1:
        print(f"{x} {y}")
        return
    
    # 제일 큰 원판을 제외한 모든 원판을 2번 칸으로 이동
    hanoi(n-1, x, 6-x-y)
    print(f"{x} {y}")
    # 나머지 원판들을 3번 칸으로 이동
    hanoi(n-1, 6-x-y, y)

if __name__ == "__main__":
    n = int(input())
    print(2 ** n - 1)
    if n <= 20:
        hanoi(n, 1, 3)