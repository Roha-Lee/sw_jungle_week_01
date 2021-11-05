import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    num = int(input())    
    nums = sorted([int(input()) for _ in range(num)])
    for n in nums:
        print(n)
    
