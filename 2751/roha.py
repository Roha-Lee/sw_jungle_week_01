import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    num = int(input())   
    # 마찬가지로 정렬 수행 
    # 앞의 정렬 1은 시간 제한 범위가 느슨하기 때문에 O(n^2)으로 풀어도 되지만 
    # sorted의 경우 O(nlogn)으로 더 빠르기 때문에 그냥 동일한 코드로 문제 해결 
    nums = sorted([int(input()) for _ in range(num)])
    for n in nums:
        print(n)
    
