import sys
input = sys.stdin.readline
n, x = map(int, input().split())
for i in map(int, input().split()):
    if i < x:
        print(i, end=' ')
print()