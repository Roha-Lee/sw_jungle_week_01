import sys
def factorial(n):
    # n! = n * (n-1)!
    # 0! = 1
    # 1! = 1
    # 2! = 2를 구현한다.
    if n == 0:
        return 1
    elif n < 3:
        return n
    return n * factorial(n-1)
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(factorial(n))