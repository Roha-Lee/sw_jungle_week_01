import sys
from itertools import combinations
'''
[6603] 로또 (https://www.acmicpc.net/problem/6603)
아이디어) 사용자로부터 입력을 받아서 모든 조합을 구한 후(itertools의 combinations함수 이용) 반환된 이터레이터를 이용하여 모든 조합을 출력한다. 
- combs : 사용자로부터 입력받은 숫자 리스트로 부터 6개를 뽑는 모든 조합에 대한 반복자
'''
def draw_numbers(nums, k=6):
    '''
    주어진 숫자 리스트에 대하여 6개의 모든 조합을 찾아서 출력하는 함수 
    Args: 
        nums(list[int]) : 사용자가 입력한 숫자의 리스트
        k(int) : 기본 값 6, 즉 6개를 추출
    Returns: 
        None
    '''
    combs = combinations(nums, k)
    for lotto in combs:
        print(*lotto)
    print()
    
if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        usr_input = list(map(int, input().split()))
        size = usr_input[0]
        if size == 0:
            break
        nums = usr_input[1:]
        draw_numbers(nums)