import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        # A와 B입력 받아서 계산 값 출력 
        A, B = map(int, input().split())
        print(A + B)
