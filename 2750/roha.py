import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    num = int(input())    
    # 숫자를 입력 받아서 정렬 수행 
    nums = sorted([int(input()) for _ in range(num)])
    for n in nums:
        print(n)
    
