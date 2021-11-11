import sys 
import math 

def is_prime(num):
    if num == 1:
        return False
    end_num = int(math.sqrt(num))
    for i in range(2, end_num + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
    print(count)
