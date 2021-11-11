import sys
import math
input = sys.stdin.readline 
a, b, v = map(int, input().split())
# 달팽이가 꼭대기에 오르려면 전체 높이에서 아침에 오를수 있는 높이를 뺀 후 
# 아침 - 저녁 거리로 나누어 준 다음 1을 더해주면 된다.(다음날 아침) 
print(math.ceil((v - a) / (a - b)) + 1)