import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

multiply = a*b*c
result = list(str(multiply))

#0~9까지 숫자 세기
#i를 문자열로 바꿔준 뒤 count로 result 리스트 안에 그 숫자가 있는지 확인하고 갯수를 출력
# for i in range(10):
#     print(result.count(str(i)))
    
count = [0] * 10
for i in range(10):
    # 결과값의 숫자 하나 하나의 인덱스를 가져옴
    # count라는 리스트의 index번호 = result숫자 에 카운팅
    count[result] += 1 
    
