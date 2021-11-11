import sys

n = int(sys.stdin.readline())
# numbers = list(range(2,1001))
input_numbers = list(map(int, sys.stdin.readline().split()))
# input_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# target : 리스트에서 없앨 배수
def removeNumber(target, list):
    cycle = 2

    while True:
        target_number = target * cycle
        # 리스트가 공백인 경우
        if not list:
            return

        # 지우고 싶은 값이 리스트안에 있는 수의 최댓값보다 큰 경우 
        if target_number > max(list):
            return
        
        # 리스트안에 내가 지우고싶은 수가 있어
        if target_number in list:
            list.remove(target_number)
        cycle += 1

# 2부터 시작, 특정 수의 모든 배수를 지운다.
# 2부터 남아있는 모든 수는 소수
# 그럼 실행 횟수는 몇 번이 좋을까?
# 지금은 범위가 1000까지니까 1000으로 하는걸로.
# 그리고 리스트가 비어있는 경우도 고려해야 함

# 1은 소수로 안 치니까 1 들어오면 빼버리기
if 1 in input_numbers:
    input_numbers.remove(1)

for i in range(2, 1001):
    removeNumber(i, input_numbers)
    # removeNumber(i, numbers)

print(len(input_numbers))