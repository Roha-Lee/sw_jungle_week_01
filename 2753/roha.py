import sys 
def is_leap_year(year):
    # 문제의 윤년 조건을 그대로 구현 
    if year % 4 == 0 and not year % 100 == 0:
        return 1
    if year % 400 == 0:
        return 1
    return 0
if __name__ == '__main__':
    input = sys.stdin.readline
    year = int(input())
    print(is_leap_year(year))

