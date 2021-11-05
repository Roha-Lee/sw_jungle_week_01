import sys 
def make_mult_table(base):
    for i in range(1, 10):
        print(f'{base} * {i} = {base * i}')
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    make_mult_table(n)

