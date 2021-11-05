import sys 
sys.setrecursionlimit(10**8)
def dfs(created_map, r, c):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rows = len(created_map)
    cols = len(created_map[0])
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and created_map[nr][nc]:
            created_map[nr][nc] = False
            dfs(created_map, nr, nc)


def count_safe_area(world, rain):
    count = 0 
    rows = len(world)
    cols = len(world[0])
    created_map = [[0]* n for _ in range(n)]
    for r in range(rows):
        for c in range(cols):
            created_map[r][c] = world[r][c] > rain

    for r in range(rows):
        for c in range(cols):
            if created_map[r][c]:
                created_map[r][c] = False
                count += 1
                dfs(created_map, r, c)

    return count
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    worlds = [[0] * n for _ in range(n)]
    start = 100
    end = 0
    
    for i in range(n):
        rows = list(map(int, input().split()))
        for j in range(n):
            worlds[i][j] = rows[j]
            start = min(start, rows[j])
            end = max(end, rows[j])    
    
    max_val = 0
    for rain in range(start-1, end):
        val = count_safe_area(worlds, rain)
        max_val = max(val, max_val)
    print(max_val)