import sys 
def hanoi(n, src=1, dst=3):
    if n > 1:
        hanoi(n-1, src, 6-src-dst)
    
    print(src, dst)
    
    if n > 1:
        hanoi(n-1, 6-src-dst, dst)
   
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(2**n - 1)
    if n <= 20:
        hanoi(n)