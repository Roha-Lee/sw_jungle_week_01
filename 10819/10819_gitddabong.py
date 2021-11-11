import sys
from itertools import combinations, permutations

def abs_sum(num1, num2):
    return abs(num1 - num2)

if __name__ == "__main__":
    input = sys.stdin.readline
    write = sys.stdout.write

    testcase = int(input())
    numbers = list(map(int, input().split()))

    maximum = 0
    # 모든 경우의 수 따져도 40000개 남짓이니까 그냥 모든 조건을 검색하는걸로.
    permutes = list(permutations(numbers, testcase))    
    for permute in permutes:
        sum = 0
        for i in range(testcase - 1):
            sum += abs_sum(permute[i], permute[i+1])

        maximum = max(maximum, sum)

    print(maximum)