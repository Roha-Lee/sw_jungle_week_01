import sys 
input = sys.stdin.readline
N, r, c = map(int, input().split())
def find_loc(N, r, c):
    if N == 0: # 종료 조건 
        return 0
    # 핵심 아이디어 : 전체를 항상 가로 세로 반씩 쪼개서 어디에 속하는지 확인
    # _r, _c는 0 또는 1로 나오며 이를 통해 사분면 중에서 어디에 있는지 확인할 수 있다. 
    _r = r // (2**(N-1)) 
    _c = c // (2**(N-1))
    # _r, _c == 0, 0 인 경우 
    #   왼쪽 위에 위치하므로 아무것도 더하지 않아도 된다. -> 2 * _r + _c == 0
    # _r, _c == 0, 1 인 경우 
    #   오른쪽 위에 위치하므로 블록 1개만 더해주면 된다. -> 2 * _r + _c == 1
    # _r, _c == 1, 0 인 경우 
    #   왼쪽 위에 위치하므로 블록 2개만 더해주면 된다. -> 2 * _r + _c == 2
    # _r, _c == 1, 1 인 경우 
    #   왼쪽 위에 위치하므로 블록 3개만 더해주면 된다. -> 2 * _r + _c == 3
    # 블록 크기 
    # -> N = 3인 경우 16(4 * 4)
    # -> N = 2인 경우 4(2 * 2)
    # -> 2 ** (N-1) * 2 ** (N-1)
    
    # 블록 크기를 계산해서 더했으면 이제 r, c의 위치를 다음 단계를 위해 바꾸어 준다. 
    # r <- r % 2**(N-1)
    # c <- c % 2**(N-1)
    
    return 2**(N-1) * 2**(N-1) * (2 * _r + _c) + find_loc(N-1, r%(2**(N-1)), c%(2**(N-1)))
print(find_loc(N, r, c))