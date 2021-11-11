import sys
from itertools import permutations

def abs_number(num1, num2):
    return abs(num1 - num2)

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    numbers = list(map(int, input().split()))

    permutes = permutations(numbers, n)

    maximum = 0
    # result_permute = None
    for permute in permutes:
        sum = 0
        for i in range(n - 1):
            sum += abs_number(permute[i], permute[i+1])
            
        # if sum > maximum: 
            # result_permute = permute
        maximum = max(maximum, sum)
    
    print(maximum)