import sys 
def hanoi(n, src=1, dst=3, count=0):
    if n == 1:
        return count + 1
    # 하노이의 탑은 n이 2이상인 모든 경우에 대하여 n을 옮기기 위해 
    # 1~(n-1)번째의 묶음을 경유지로 옮긴 후 
    if n > 1:
        count = hanoi(n-1, src, 6-src-dst, count)
    
    # n을 도착지로 옮긴후 
    print(src, dst)
    count += 1
    
    # 다시 1~(n-1)묶음을 도착지로 옮긴다. 
    if n > 1:
        count = hanoi(n-1, 6-src-dst, dst, count)
    return count 
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    # 하노이의 탑 횟수를 구하는 공식은 2 ^ n - 1로 알려져 있다. 
    # n이 20 이하인 경우 옮기는 방식을 출력하기 위해 아래 하노이 함수를 실행한다. 
    print(2**n - 1)
    if n <= 20:
        hanoi(n)