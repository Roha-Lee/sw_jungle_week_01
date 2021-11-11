import sys
sys.setrecursionlimit(10**8)

# n * n 만큼 모든 행렬을 돌면서 안전 영역의 카운트를 세서 return 
def search_all_sz(n):
    count = 0
    for i in range(n):
        for j in range(n):
            if catch_safe_zone(i, j):
                count += 1
    return count

# 출발점 x,y에서 시작해 만들 수 있는 안전영역이 하나 있으면 True, 아니면 False 출력
def catch_safe_zone(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= testcase or y <= -1 or y >= testcase:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if field[x][y] == 1:
        field[x][y] = 0

        # 상하좌우의 위치 모두 재귀적으로 호출
        catch_safe_zone(x-1, y)
        catch_safe_zone(x, y-1)
        catch_safe_zone(x+1, y)
        catch_safe_zone(x, y+1)
        return True
    return False

if __name__ == "__main__":
    input = sys.stdin.readline

    testcase = int(input())
    buildings = []
    field = [[-1 for _ in range(testcase)] for _ in range(testcase)]
    for i in range(testcase):
        buildings.append(list(map(int, input().split())))

    sz_max = 0
    for height in range(101):
        # 특정 높이에 물이 찰 경우의 필드를 시뮬레이션
        for i in range(testcase):
            for j in range(testcase):
                if buildings[i][j] > height:
                    field[i][j] = 1
                else:
                    field[i][j] = 0
        
        # all_sz_count = search_all_sz(testcase)
        # if all_sz_count == 0:
        #     break
        # else:
        #     sz_max = max(sz_max, all_sz_count)
        all_sz_count = search_all_sz(testcase)
        sz_max = max(sz_max, all_sz_count)
        
    print(sz_max)