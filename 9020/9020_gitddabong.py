import sys

prime_numbers = list(range(2,10001))
def removeNumber(target, list):
    cycle = 2

    while True:
        target_number = target * cycle
        if not list:
            return

        if target_number > max(list):
            return
        
        if target_number in list:
            list.remove(target_number)
        cycle += 1

# 2부터 n까지의 리스트를 소수 리스트로 만드는 함수
def make_prime_numbers(list):
    if 1 in list:
        list.remove(1)

    i = 0
    while True:
        if not list:
            print("list is empty!")
            return

        if list[i] >= max(list):
            return

        removeNumber(list[i], list)
        i += 1

make_prime_numbers(prime_numbers)

n = int(sys.stdin.readline())
goldbach = []
for i in range(n):
    goldbach.append(int(sys.stdin.readline()))

# 골드바흐의 추측 : 모든 짝수에 대한 소수의 합이 존재한다.
# 합이 여러개일 경우 두 수의 차가 최솟값인 짝을 고를 것

# 주어진 n을 절반으로 나누어 수가 낮은 쪽으로 가면서 짝찾기
# 사실 성능을 개선하려면 나누어서 인덱스 적은 쪽으로 가는게 맞는데, 거기까진 안해도 될 것 같음
for i in range(n):
    # 반값에서 1씩 빼면서 근사한 소수 찾기 
    target = int(goldbach[i] / 2)       # 나눠보니 정수가 아니고 실수더라

    while True:
        if target in prime_numbers:
            break
        else:
            target -= 1

    index = prime_numbers.index(target)
    # 찾은 소수로 짝찾기
    while True:
        if index == -1:
            break

        if goldbach[i] - prime_numbers[index] in prime_numbers:
            print(str(prime_numbers[index]) + " " + str(goldbach[i] - prime_numbers[index]))
            break
        else:
            index -= 1