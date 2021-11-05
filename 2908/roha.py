import sys 
def sangsoo_ans(a, b):
    a = a[::-1]
    b = b[::-1]
    for dig_a, dig_b in zip(a, b):
        if dig_a > dig_b:
            return a
        elif dig_b > dig_a:
            return b

if __name__ == '__main__':
    input = sys.stdin.readline
    a, b = input().split()
    print(sangsoo_ans(a, b))