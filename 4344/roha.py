import sys 
def over_average(scores):
    # 평균을 구한다. 
    average = sum(scores) / len(scores)
    # 평균 이상인 사람을 센다. 
    count = 0
    for score in scores:
        if score > average:
            count += 1
    # 백분율로 반환한다.
    return count / len(scores) * 100

if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        user_input = list(map(int, input().split()))
        num_user = user_input[0]
        scores = user_input[1:]
        # formatted string을 이용하여 결과를 출력한다.
        print('%.3f%%'%(over_average(scores)))
