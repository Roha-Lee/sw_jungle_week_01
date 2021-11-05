import sys 
input = sys.stdin.readline
count = [0] * 10 
A = int(input())
B = int(input())
C = int(input())
multiplication = A * B * C
while multiplication > 0:
    count[multiplication % 10] += 1
    multiplication //= 10

for i in count:
    print(i)