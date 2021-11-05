import sys 
def over_average(scores):
    average = sum(scores) / len(scores)
    count = 0
    for score in scores:
        if score > average:
            count += 1
    return count / len(scores) * 100
if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        user_input = list(map(int, input().split()))
        num_user = user_input[0]
        scores = user_input[1:]
        print('%.3f%%'%(over_average(scores)))
