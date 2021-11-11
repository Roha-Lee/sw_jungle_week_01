import sys

def search(past = 0, count = 0, total_cost = 0, start = 0):
    global total_min
    # 모든 노드를 방문한 경우
    if count == n:
        # 다음 경로에 길이 없는 경우 return
        if paths[past][start] != 0:
            total_min = min(total_cost + paths[past][start], total_min)
        return

    for i in range(n):
        # 이번 노드를 방문하지 않은 경우 알고리즘 진행
        if visits[i] == False:
            # 다음 경로에 길이 없는 경우, 지금까지의 경로의 합이 최솟값보다 높을 경우 (더 볼필요 없음) 더 이상 진행 X
            if count == 0 or (paths[past][i] != 0 and total_min > total_cost + paths[past][i]):
                # 시작점을 저장하기 위한 조건문
                if count == 0:
                    start = i
                    past = i
                visits[i] = True
                search(i, count + 1, total_cost + paths[past][i], start)
                visits[i] = False
        

if __name__ == "__main__":
    input = sys.stdin.readline

    total_min = 10000005

    n = int(input())
    # 모든 경로의 정보가 저장된 리스트
    paths = []
    # 경로를 방문했는지 아닌지를 판별하는 리스트
    visits = [False] * n
    for i in range(n):
        paths.append(list(map(int, input().split())))

    search()
    print(total_min)
    