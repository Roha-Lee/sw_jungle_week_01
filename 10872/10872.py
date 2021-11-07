import sys
input = sys.stdin.readline

def facto(n):
    if n == 0:
        return 1
    if n < 3:
        return n
    else:
        return n * facto(n-1)

n = int(input())
print(facto(n))