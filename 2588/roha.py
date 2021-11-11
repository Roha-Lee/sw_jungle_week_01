import sys 
def multiplication(num1, num2):
    total = 0
    m_const = 1
    # 곱셈을 구하기 위해 일의자리부터 순차적으로 얻음 (num2 % 10)
    # num1 과 곱하여 각 자리수의 곱셈 결과를 만들어 냄
    # 전체 결과를 얻기 위해 m_const와 곱해서 total에 더해줌 
    # m_const는 1, 10, 100, 1000으로 10배씩 커짐
    # num2를 10으로 나누어서 다음 연산을 준비 
    while num2 > 0:
        cur_val = num1 * (num2 % 10)
        print(cur_val)
        total += cur_val * m_const
        m_const *= 10
        num2 //= 10

    return total
    
if __name__ == '__main__':
    input = sys.stdin.readline
    num1 = int(input())
    num2 = int(input())
    result = multiplication(num1, num2)
    print(result)