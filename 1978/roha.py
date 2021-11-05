import sys 
import math
# 소수 판별법
def is_prime(num):
    if num == 1: 
        return False
    if num == 2:
        return True
        
    end_point = int(math.sqrt(num))
    # 대칭성때문에 루트 n까지만 나누어 떨어지는지 확인하면 됨
    for i in [2] + list(range(3, end_point + 1, 2)):
        # 하나라도 나누어 떨어지면 소수가 아니므로 False
        if num % i == 0:
            return False
    # 전부 나누어 떨어지지 않으면 True
    return True

if __name__ == '__main__':
    input = sys.stdin.readline
    num = int(input())
    num_list = list(filter(is_prime, map(int, input().split())))
    print(len(num_list))