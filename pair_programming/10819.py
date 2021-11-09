import sys
from itertools import permutations

def abs_number(num1, num2):
    return abs(num1 - num2)

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    numbers = sorted(list(map(int, input().split())))

    permutes = permutations(numbers, n)

    maximum = 0
    result_permute = None
    for permute in permutes:
        sum = 0
        for i in range(n - 1):
            sum += abs_number(permute[i], permute[i+1])
            
        if sum > maximum: 
            result_permute = permute
        maximum = max(maximum, sum)
        
    result = [0] * n
    mid = n // 2
    result[-1] = numbers[mid]
    result[0] = numbers[mid - 1]
    
    for i in range(1, mid):
        result[2 * i] = numbers[i - 1]
        result[2 * i - 1] = numbers[mid + i]        
    
    print(numbers)
    print("maximum_val", maximum)
    print("using greedy(maybe)", result)
    print("using permutation", result_permute)
    
# #     print(maximum)
# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n = int(input())
#     nums = sorted(list(map(int, input().split())))
    