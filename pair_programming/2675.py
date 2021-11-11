import sys
input = sys.stdin.readline
n = int(input())
def repeat_str(input_str, k):
    result_str = ''
    for letter in input_str:
        result_str += letter * k
    return result_str

# 모든 테스트 케이스의 반복에 필요한 반복문
for i in range(n):
    str_num, text = input().split()
    num = int(str_num)
    
    # 텍스트의 종류만큼 반복에 필요한 반복문
    for j in range(len(text)): 
        # 주어진 횟수만큼 한 글자를 반복시키는 반복문
        for k in range(num):
            print(text[j], end="")
    print("\n", end="")