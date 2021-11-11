import sys 
from itertools import permutations
'''
[2503] 로또 (https://www.acmicpc.net/problem/2503)
아이디어) 먼저 주고받은 질문 답변을 ball로 먼저 내림차순 정렬하고 strike로 다시 내림차순 정렬하여 
맨 처음 가장 많은 경우의 수를 거를 수 있게 한다. 
- perms: 가능한 모든 경우의 수 
- valid: 각 경우의 수의 유효성을 체크하기 위한 list[bool]

모든 경우의 수에 대하여 먼저 살아남은 숫자인지 확인하고(valid[i]가 True인지 확인) 살아있는 수 중에서
is_correct_answer함수를 통해 주고받은 답변과 모순이 없는지 확인한 후 모순이 있으면 valid[i]를 False로 바꾸어준다.  
이 때 and 연산자로 두 조건을 묶었기 때문에 앞쪽(valid[i])이 False이면 뒤 조건을 실행조차 하지 않고 넘어간다.
마지막으로 valid의 합을 구하게 되면 True -> 1, False -> 0이므로 유효한 경우의 수를 얻을 수 있게 된다. 
'''

def is_correct_answer(ans, query, strike, ball):
    '''
    정답(ans), 질문(query)가 들어왔을 때 스트라이크, 볼 값을 계산하고 이를 입력된 strike, ball과 일치하는 지 확인하는 함수 
    
    Args: 
        ans(Sequence): 정답
        query(Sequence): 질문
        strike(int): 입력으로 들어온 스트라이크 
        ball(int): 입력으로 들어온 볼
    Returns: 
        bool, 일치하면 True, 아니면 False
    '''
    ball_list = [False] * 3
    strike_list = [False] * 3
    for i in range(3):
        strike_list[i] = ans[i] == query[i]
        ball_list[i] = query[i] in ans
    
    calc_strike = sum(strike_list)
    # 423, 432가 나왔을때 sum(ball_list) = 3, sum(strike_list) = 1이므로 
    # 1 strike, 2 ball을 만들어준다. 
    calc_ball = sum(ball_list) - sum(strike_list)
    if calc_ball == ball and calc_strike == strike:
        return True
    return False
    
def count_possible_cases(questions):
    '''
    주어진 질문/답변에 대하여 답의 가능성이 있는 경우를 세는 함수

    Args:
        questions(list[tuple[tuple[int], int, int]]) : 질문과 답변에 대한 정보들
    Returns:
        int : 경우의 수 
    '''
    perms = list(permutations(range(1, 10), 3))
    valid = [True] * len(perms)
    for query, strike, ball in questions:
        for i in range(len(perms)):
            if valid[i] and not is_correct_answer(perms[i], query, strike, ball):
                valid[i] = False

    return sum(valid)

if __name__ == '__main__':
    input = sys.stdin.readline
    turn = int(input())
    questions = []
    
    for _ in range(turn):
        query, strike, ball = input().split()
        strike, ball = int(strike), int(ball)
        query = tuple(map(int, query))
        questions.append((query, strike, ball))

    sorted(questions, key = lambda x: x[2], reverse = True)
    sorted(questions, key = lambda x: x[1], reverse = True)
    print(count_possible_cases(questions))