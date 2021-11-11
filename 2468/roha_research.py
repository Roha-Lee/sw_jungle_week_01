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

def get_next_location(worlds, mid, DP, left, right):
    DP[mid] = count_safe_area(worlds, mid)
    prev_count, next_count = DP[mid], DP[mid]
    prev, next = 1, 1

    while prev_count == DP[mid] and next_count == DP[mid] :
        if mid - prev >= 0:
            if not DP[mid - prev]:
                DP[mid - prev] = count_safe_area(worlds, mid - prev)
            prev_count = DP[mid - prev]
            prev += 1
        if mid + next <= 100:
            if not DP[mid + next]:
                DP[mid + next] = count_safe_area(worlds, mid + next)
            next_count = DP[mid + next]
            next += 1
    
    if prev_count < DP[mid] and DP[mid] <= next_count:
        return mid + 1, right

    elif prev_count > DP[mid] and DP[mid] >= next_count:
        return left, mid - 1
    
    elif prev_count <= DP[mid] and DP[mid] < next_count:
        return mid + 1, right
    
    elif prev_count >= DP[mid] and DP[mid] > next_count:
        return left, mid - 1

    else: 
        return mid + 1, mid - 1        

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
    
    # DP = [0] * 101
    # left, right = min_val - 1, max_val 
    # while left <= right:
    #     mid = (left + right) // 2
    #     left, right = get_next_location(worlds, mid, DP, left, right)

    # binsear = max(DP)

    best = 0
    for rain in range(min_val-1, max_val):
        best = max(best, count_safe_area(worlds, rain))
    
    