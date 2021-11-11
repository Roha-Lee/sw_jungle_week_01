import sys 

def make_mult_table(base):
    # 1부터 9까지 i를 생성하고 곱셈값을 얻은 후 formatted string을 이용하여 출력 
    for i in range(1, 10):
        print(f'{base} * {i} = {base * i}')
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    make_mult_table(n)

