import sys 
def multiplication(num1, num2):
    total = 0
    m_const = 1
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