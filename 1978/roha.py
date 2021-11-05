import sys 
import math
def is_prime(num):
    if num == 1: 
        return False
    if num == 2:
        return True
        
    end_point = int(math.sqrt(num))
    for i in [2] + list(range(3, end_point + 1, 2)):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    input = sys.stdin.readline
    num = int(input())
    num_list = list(filter(is_prime, map(int, input().split())))
    
    print(len(num_list))