import sys 
from itertools import permutations
def get_value(nums):
    total = 0
    for i in range(1, len(nums)):
        total += abs(nums[i] - nums[i-1])
    return total

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    nums_list = permutations(nums)
    max_val = 0
    for nums in nums_list:
        max_val = max(max_val, get_value(nums))
    print(max_val)