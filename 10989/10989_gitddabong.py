import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
numbers = [0] * 10001

for _ in range(n):
    num = int(input())
    numbers[num] += 1

for i in range(10001):
    if numbers[i] == 0:
        continue
    else:
        for j in range(numbers[i]):
            write(str(i) + "\n")