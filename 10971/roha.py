import sys 
def dfs(root, src, costs, visited, cost=0):
    global curr_min
    if cost > curr_min:
        return
    if sum(visited) == n:
        if cost_matrix[src][root]:
            costs.append(cost + cost_matrix[src][root])
            curr_min = cost + cost_matrix[src][root]
        return
    
    for dst in range(n):
        if visited[dst] or not cost_matrix[src][dst]:
            continue
        visited[dst] = True
        dfs(root, dst, costs, visited, cost + cost_matrix[src][dst])
        visited[dst] = False
        
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    cost_matrix = []
    for _ in range(n):
        rows = list(map(int, input().split()))
        cost_matrix.append(rows)
    costs = []
    visited = [False] * (n+1)
    curr_min = float("inf")
    for root in range(n):
        visited[root] = True
        dfs(root, root, costs, visited)
        visited[root] = False
    print(min(costs))

