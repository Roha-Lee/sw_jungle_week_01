import sys 
def make_stair(num):
    for i in range(1, num+1):
        print('*' * i)
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    make_stair(n)
