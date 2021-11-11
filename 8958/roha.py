import sys 
def get_score(results):
    # 한 줄에 대한 점수를 계산하는 함수
    score = 1
    total_score = 0
    for ans in results:
        # X를 만나면 점수를 1로 초기화 해 준다. 
        if ans == 'X':
            score = 1
        # O를 만나면 총점에 점수를 더하고 점수를 1 증가시킨다. 
        else:
            total_score += score
            score += 1
    return total_score
    
if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        print(get_score(input().rstrip()))
    