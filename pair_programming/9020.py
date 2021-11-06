# -*- coding:utf-8 -*- 
import sys 
import math
def eratos_sieve(n):
    # 소수를 걸러낼 리스트 (처음에는 2부터 n까지 모든 수가 들어있지만 소수가 아닌 수를 모두 제거해서 소수만 남길 예정)
    prime_numbers = list(range(2, n+1))

    idx = 0
    # target = 2      # 배수. 2의 배수를 없애고 싶으면 target = 2
    
    while True:
        if prime_numbers[idx] >= prime_numbers[-1]:
            break
        target = prime_numbers[idx]
        num = 2         # 리스트 안에서 배수를 없앨 때 1씩 증가시켜서 배수를 구할 때 사용하는 변수
        while True:
            # 만약에 내가 없애고 싶은 숫자가 리스트 안에 있다면
            # 그 수를 제거
            if target * num in prime_numbers:
                prime_numbers.remove(target * num) # -> O(N)
            else:
                pass
            
            # 루프 탈출조건. target * num 이 리스트 안에 들어있는 최댓값보다 같거나 크면 종료
            # 왜 굳이 인덱스 안쓰고 이렇게 하냐?
            # remove() 를 통해서 계속해서 원소를 삭제하고 있기 때문에 index가 계속 앞으로 당겨옴.
            # 그래서 리스트에서 가장 큰 값을 만나면 멈추는 것으로 결정.
            if target * num >= prime_numbers[-1]:
                break

            num += 1
        # target += 1
        idx += 1

    return prime_numbers

def eratos_sieve2(n):
    prime_numbers = [True] * (n+1)
    prime_numbers[0] = False
    prime_numbers[1] = False

    end_num = int(math.sqrt(n))
    for current in range(2, end_num+1):
        if not prime_numbers[current]:
            continue
        
        i = 2
        while current * i <= n:
            prime_numbers[current*i] = False
            i += 1
    
    return prime_numbers


def goldbach(n):
    prime_numbers = eratos_sieve2(n)    
    for num in range(n // 2, 0, -1):
        if prime_numbers[num] and prime_numbers[n-num]:
            return num, n-num

if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        print(*goldbach(n))
    
                    
    