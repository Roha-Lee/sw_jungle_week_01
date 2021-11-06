import sys 
def get_grade(score):
    # 구간마다 알맞은 성적을 반환해준다. 
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'
    

if __name__ == '__main__':
    input = sys.stdin.readline
    score = int(input())
    print(get_grade(score))