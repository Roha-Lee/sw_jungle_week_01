import sys 
def create_map(worlds, rain):
    return  [ list(map(lambda x: x > rain, world)) for world in worlds ]        
    
def count_safe_area(worlds, rain):
    current_map = create_map(worlds, rain)
    rows = len(worlds)
    cols = len(worlds[0])
    count = 0 
    for r in range(rows):
        for c in range(cols):
            if current_map[r][c]:
                count += 1
                remove_one_island(current_map, r, c)
    return count 

def remove_one_island(current_map, r, c):
    # 동, 남, 서, 북으로 움직이는 방향 정하기 
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    rows = len(current_map)
    cols = len(current_map[0])
    for dr, dc in moves:
        new_r, new_c = r + dr, c + dc
        #       new_r, new_c가 범위 안에 있음                    육지
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

