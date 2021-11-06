import sys 
from itertools import permutations
def get_value(nums):
    # 배열이 주어졌을때 문제의 식의 값을 구해준다. 
    total = 0
    for i in range(1, len(nums)):
        total += abs(nums[i] - nums[i-1])
    return total

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    # 모든 경우의 수의 숫자 배열을 생성한다. 
    nums_list = permutations(nums)
    max_val = 0
    # 최대값을 구한다.
    for nums in nums_list:
        max_val = max(max_val, get_value(nums))
    print(max_val)