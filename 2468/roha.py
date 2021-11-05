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
    # created_map을 통해 하고자 하는 것: 비에 잠기는 부분은 False, 잠기지 않는 부분은 True인 맵을 만듦
    created_map = [[0]* n for _ in range(n)]
    for r in range(rows):
        for c in range(cols):
            created_map[r][c] = world[r][c] > rain
    # 순회하다 True인 부분을 만나면 False로 바꾸어 주고 그 부분과 연결된 모든 안전지대를 False로 바꿈
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
    # 월드 정보를 얻으면서 높이의 최소값과 최대값을 각각 start, end에 저장
    for i in range(n):
        rows = list(map(int, input().split()))
        for j in range(n):
            worlds[i][j] = rows[j]
            start = min(start, rows[j])
            end = max(end, rows[j])    
    # start - 1부터 end까지 한번씩 안전지대 계산을 하여 최대값을 구함 
    # start - 1 인 이유는 아래와 같은 케이스 때문 
    '''
    2
    1 1
    1 1 일때 정답이 0이 아니라 1임. 
    '''
    max_val = 0
    for rain in range(start-1, end):
        val = count_safe_area(worlds, rain)
        max_val = max(val, max_val)
    print(max_val)