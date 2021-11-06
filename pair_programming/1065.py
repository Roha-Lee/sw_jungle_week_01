import sys

def get_digits(num):
    digits = []
    while num > 0: 
        digits.append(num % 10)
        num //= 10 
    return digits

def is_hansu(n):
    # is_hansu : snake case
    # isHansu : Camel case
    # IsHansu : Pascal case
    # is-hansu : kebab case

    if n < 100:
        return True

    # n100 = n // 100
    # n10 = (n % 100) // 10
    # n1 = n % 10

    # 수가 등차수열인지 아닌지 확인하기 위한 각 자리수의 차를 비교
    numbers = get_digits(n)
    term = numbers[0] - numbers[1]
    for i in range(1, len(numbers)-1):
        if numbers[i] - numbers[i+1] != term:
            return False
    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    
    count = 0
    for i in range(1, n+1):
        if is_hansu(i):
            count += 1

    print(count)
