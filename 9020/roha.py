import sys 
import math 
def eratosthenes_sieve(x):
    prime = [True] * (x+1)
    for i in range(2, math.ceil(math.sqrt(x))):
        if prime[i]:
            j = 2
            while i * j <= x:
                prime[i * j] = False
                j += 1
    return prime

def partition(n):
    primes = eratosthenes_sieve(n)
    mid = n // 2
    first = mid if n % 2 == 0 else mid + 1
    second = mid
    while second >= 2:
        if primes[first] and primes[second]:
            return second, first
        first += 1
        second -= 1
if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        print(*partition(int(input())))

