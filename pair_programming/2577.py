import sys 

def count_digit(num):
    count = [0] * 10
    while num > 0: 
        count[num % 10] += 1
        num //= 10 
    return count

def count_digit2(string):
    count = [0] * 10
    digit_list = list(string)
    for letter in digit_list:
        count[int(letter)] += 1
    return count
    
if __name__ == '__main__':
    input = sys.stdin.readline
    A = int(input())
    B = int(input())
    C = int(input())

    result = count_digit(A*B*C)
    result2 = count_digit2(str(A*B*C))
    for i in result:
        print(i)