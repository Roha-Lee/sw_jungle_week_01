import sys
input = sys.stdin.readline
width, height = map(int, input().split())
num = int(input())
# 가로 길이의 최대값, 세로 길이의 최대값을 찾기 위해 아래와 같이 절취선 좌표를 저장 
# 0, height를 저장한 이유는 추후에 인접한 원소의 차를 구하여 각각의 길이를 구한 후 이 중 최대값을 찾아내기 위함
vertical = [0, height]
horizontal = [0, width]
for _ in range(num):
    vh, index = map(int, input().split())
    if vh == 0: # 가로 
        vertical.append(index)
    else: # 세로 
        horizontal.append(index)

# 오름차순 정렬
vertical.sort()
horizontal.sort()

final_width = 0
final_height = 0 
# 가장 큰 가로, 세로 값을 찾아서 곱하여 최대 면적을 구해줌 
for i in range(1, len(vertical)):
    final_width = max(vertical[i] - vertical[i-1], final_width)
for i in range(1, len(horizontal)):
    final_height = max(horizontal[i] - horizontal[i-1], final_height)

print(final_height * final_width)
