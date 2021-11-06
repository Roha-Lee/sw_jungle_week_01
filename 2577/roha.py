import sys 
input = sys.stdin.readline
# 0부터 9까지 개수를 셀 배열 생성
count = [0] * 10 
A = int(input())
B = int(input())
C = int(input())
multiplication = A * B * C
# 각 자리수의 숫자를 1씩 증가시킴
while multiplication > 0:
    count[multiplication % 10] += 1
    multiplication //= 10

for i in count:
    print(i)