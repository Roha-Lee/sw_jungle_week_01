import sys
input = sys.stdin.readline
n, x = map(int, input().split())
for i in map(int, input().split()):
    # x 보다 작은 값을 출력한다.
    if i < x:
        print(i, end=' ')
print()