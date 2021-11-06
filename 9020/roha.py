import sys 
import math 
def eratosthenes_sieve(x):
    # x 이하의 소수를 전부 구하는 에라토스테네스의 체 알고리즘 구현 
    prime = [True] * (x+1)
    for i in range(2, math.ceil(math.sqrt(x))):
        if prime[i]:
            j = 2
            while i * j <= x:
                prime[i * j] = False
                j += 1
    return prime


def partition(n):
    # n이하의 소수를 전부 구한다. 
    primes = eratosthenes_sieve(n)
    
    # 차이가 가장 적은 두 수부터 스캔하기 위해 시작점을 계산한다. 
    mid = n // 2
    first = mid if n % 2 == 0 else mid + 1
    second = mid
    
    # 두 수 모두 소수인 경우 결과를 반환
    while second >= 2:
        if primes[first] and primes[second]:
            return second, first
        first += 1
        second -= 1


if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        # 결과가 tuple로 나오기 때문에 *를 이용하여 튜플을 풀어준다. 
        print(*partition(int(input())))

