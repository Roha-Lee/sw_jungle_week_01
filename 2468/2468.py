import sys 
def create_map(worlds, rain):
            # worlds의 world(한줄씩)에서 x가 rain보다 크면 True. / map은 world의 하나하나 원소. -> 원소 하나하나에 x>rain(T/F) 적용
    return  [ list(map(lambda x: x > rain, world)) for world in worlds ]        
    
def count_safe_area(worlds, rain):
    current_map = create_map(worlds, rain)
    rows = len(worlds)    #행의 갯수
    cols = len(worlds[0]) #행 하나의 갯수를 세서 총 "열"(세로)이 몇개인지 > n으로 세도 됨
    count = 0 
    for r in range(rows): 
        for c in range(cols):
            if current_map[r][c]: #r은 세로로 찾고 c는 가로로 찾는다 (r,c)를 찾음
                count += 1        #True인 섬을 만나면 증가
                remove_one_island(current_map, r, c) #섬이랑 연결된 곳을 False로 바꿈(이미 셌으니까)
    return count 

def remove_one_island(current_map, r, c):
    # 동, 남, 서, 북으로 움직이는 방향 정하기 
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    rows = len(current_map)    #행의 갯수
    cols = len(current_map[0]) #행 하나의 갯수를 세서 총 "열"(세로)이 몇개인지 > n으로 세도 됨
    for dr, dc in moves:       #d는 델타(변화량)
        #최종 이동한 좌표값(다음 갈 좌표값)
        new_r, new_c = r + dr, c + dc #현재의 r,c에 이동량을 1칸씩 (moves)더함
        #       new_r, new_c가 맵 범위 안에 있음                    육지(True)
        if not (0 <= new_r < rows and 0 <= new_c < cols and current_map[new_r][new_c]):
            continue
        
        current_map[new_r][new_c] = False
        remove_one_island(current_map, new_r, new_c)

if __name__ == '__main__':
    sys.setrecursionlimit(10**8)
    input = sys.stdin.readline
    n = int(input())
    
    min_val = float("inf")
    max_val = 0
    
    worlds = []
    for _ in range(n):
        rows = list(map(int, input().split()))
        max_val = max(max_val, max(rows))
        min_val = min(min_val, min(rows))
        worlds.append(rows)
    
    best = 0
    for rain in range(min_val - 1, max_val + 1):
        best = max(best, count_safe_area(worlds, rain))
    print(best)

    # best = 0
    # # DP = [0] * 
    # while min_val <= max_val:
    #     mid = (max_val + min_val) // 2
    #     count = count_safe_area(worlds, mid)
    #     if best < count: 
    #         best = count