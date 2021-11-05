import sys
from typing import final 
input = sys.stdin.readline
width, height = map(int, input().split())
num = int(input())
vertical = [0, height]
horizontal = [0, width]
for _ in range(num):
    vh, index = map(int, input().split())
    if vh == 0: # 가로 
        vertical.append(index)
    else: # 세로 
        horizontal.append(index)
vertical.sort()
horizontal.sort()
final_width = 0
final_height = 0 
for i in range(1, len(vertical)):
    final_width = max(vertical[i] - vertical[i-1], final_width)
for i in range(1, len(horizontal)):
    final_height = max(horizontal[i] - horizontal[i-1], final_height)

print(final_height * final_width)
