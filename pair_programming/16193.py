# import sys

# def get_value(nums):
#     # 배열이 주어졌을때 문제의 식의 값을 구해준다. 
#     total = 0
#     for i in range(1, len(nums)):
#         total += abs(nums[i] - nums[i-1])
#     return total

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n = int(input())
#     numbers = sorted(list(map(int, input().split())))
#     result = [0] * n
#     mid = n // 2
#     result[-1] = numbers[mid]
#     result[0] = numbers[mid - 1]
#     endpoint = mid if n % 2 == 0 else mid + 1
#     for i in range(1, endpoint):
#         if not 2 * i == n-1:
#             result[2 * i] = numbers[i - 1]
        
#         result[2 * i - 1] = numbers[mid + i]        
    
#     print(get_value(result))
    

import sys 
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = deque(sorted(list(map(int, input().split()))))
    result = deque([nums.popleft()])
    
    sum_ = 0
    while nums:
        num1 = abs(result[0] - nums[0])
        num2 = abs(result[0] - nums[-1])
        num3 = abs(result[-1] - nums[0])
        num4 = abs(result[-1] - nums[-1])
        max_num = max(num1, num2, num3, num4)

        if max_num == num1:
            result.appendleft(nums.popleft())
            sum_ += num1
        elif max_num == num2:
            result.appendleft(nums.pop())
            sum_ += num2
        elif max_num == num3:
            result.append(nums.popleft())
            sum_ += num3
        else:
            result.append(nums.pop())
            sum_ += num4
    print(sum_)