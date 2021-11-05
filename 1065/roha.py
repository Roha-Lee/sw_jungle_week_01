import sys 
def is_hansu(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n //= 10
    if len(digits) < 3:
        return True
    else:
        diff = digits[1] - digits[0]
        for i in range(2, len(digits)):
            if diff != digits[i] - digits[i-1]:
                return False
        return True

if __name__ == '__main__':
    input = sys.stdin.readline 
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if is_hansu(i):
            count += 1
    print(count)