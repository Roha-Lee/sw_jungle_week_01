import sys 
input = sys.stdin.readline
n = int(input())
def n_queen(x):
    global results
    # n개를 전부 놓은경우 results 값 1증가 
    if x == n:
        results += 1
    else:
        for col in range(n):
            # 이미 사용된 col인 경우 바로 종료 
            if col not in used:
                # 합이 같은 경우
                val1 = x + col
                # 차가 같은 경우 
                val2 = x - col + n - 1
                # 이미 사용된 대각선이면 바로 종료 -> 원래는 row - col찾는 O(n)으로 수행하려 했는데 시간초과..
                # O(1)로 변경 
                if not diag1[val1] and not diag2[val2]:
                    diag1[val1] = True 
                    diag2[val2] = True
                    used.add(col)
                    # 다음 row로 이동
                    n_queen(x+1)
                    used.remove(col)
                    diag1[val1] = False
                    diag2[val2] = False
                    
# 이미 사용된 col인지 확인
used = set()
# 이미 사용된 대각선인지 확인
diag1 = [False] * (2*n-1)
diag2 = [False] * (2*n-1)
results = 0
# 0번 row부터 시작 
n_queen(0)
print(results)
