import sys

def dfs(list, row = 0, sum = 0):
    if row == len(list):
        return

    for i in range(len(list)):
        # False : 아직 가보지 않음, True : 갔다 왔음
        if not visits[row][i] or paths[row][i] == 0:
            visits[row][i] = True
            sum += paths[row][i]

            dfs(list, row + 1, sum)

            visits[row][i] = False

    return sum

paths = []
if __name__ == "__main__":
    n = int(input())
    visits = [[False for _ in range(n)] for _ in range(n)]

    total_sum = 0
    for i in range(n):
        paths.append(list(map(int, input().split())))
    
    print(dfs(paths))