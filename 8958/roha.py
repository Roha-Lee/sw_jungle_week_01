import sys 
def get_score(results):
    score = 1
    total_score = 0
    for ans in results:
        if ans == 'X':
            score = 1
        else:
            total_score += score
            score += 1
    return total_score
    
if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        print(get_score(input().rstrip()))
    