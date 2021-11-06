import sys 
def sangsoo_ans(a, b):
    # 상수가 숫자를 거꾸로 읽기 때문에 두 스트링을 뒤집어 준다. 
    a = a[::-1]
    b = b[::-1]
    # 각 자리수에 대하여 비교 연산을 수행하여 하나라도 큰 수가 나올 경우 그 수로 반환해준다. 
    # 단, 여기서는 두 숫자가 모두 세자리이기 때문에 자리수만 비교해도 결과값을 얻을 수 있다. 
    # for dig_a, dig_b in zip(a, b):
    #     if dig_a > dig_b:
    #         return a
    #     elif dig_b > dig_a:
    #         return b
    return a if a > b else b
if __name__ == '__main__':
    input = sys.stdin.readline
    a, b = input().split()
    print(sangsoo_ans(a, b))