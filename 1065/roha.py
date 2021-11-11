import sys 
def is_hansu(n):
    # 각 자리수를 리스트에 담음 
    digits = []
    while n > 0:
        digits.append(n%10)
        n //= 10

    # 리스트의 길이가 3 미만이면 항상 참
    if len(digits) < 3:
        return True
    else:
        # 1번째 - 0번째로 공차를 구하고 2번째부터 i번째에서 i-1번째를 뺀 것을 계산하여 한번이라도 다르면 False
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
        if is_hansu(i): # 1부터 n까지 반복하며 i가 한수인지 확인
            count += 1
    print(count)