import sys
input = sys.stdin.readline

width, height = map(int, input().split())
testcase = int(input())

h_list = [height]
v_list = [width]

for i in range(testcase):
    vh, location = map(int, input().split())
    if vh == 0:
        h_list.append(location)
    else:
        v_list.append(location)

h_list.sort()
v_list.sort()

h_max = h_list[0]
v_max = v_list[0]

for i in range(len(h_list) - 1):
    h_max = max(h_list[i+1] - h_list[i], h_max)

for i in range(len(v_list) - 1):
    v_max = max(v_list[i+1] - v_list[i], v_max)

print(h_max * v_max)