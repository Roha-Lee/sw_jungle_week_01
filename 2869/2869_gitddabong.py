import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

target = v - a      # 한 번에 a만큼 갈 수 있으니까 a만큼 미리 빼면 몇 번을 갈 수 있을지 확인
one_day = a - b     # 하루에 갈 수 있는 거리

# 하루에 몇 번 갈 수 있는지 계산
# 만약 남은 거리가 10이고 하루에 갈 수 있는 거리가 3이라면 
# 이 둘을 나누면 3.@@@ 가 되지만, 아주 약간의 거리가 남더라도 하루는 더 가야하기 때문에 소수점은 올림해준다.
print(math.ceil(target / one_day) + 1)