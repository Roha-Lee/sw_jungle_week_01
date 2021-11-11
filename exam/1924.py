import sys 
'''
[1924] 2007년 (https://www.acmicpc.net/problem/1924)

아이디어) 입력된 x월 x일과 1월 1일의 일 수 차이를 구해서 7로 나눈 나머지를 이용해서 요일을 구한다. 

- day_max: 각 월에 해당하는 최대 일수 
- day_of_week: 요일에 해당하는 문자열이 담긴 리스트
- num_days: x월 x일의 총 일 수 
1월 1일은 1일차 이므로 num_days - 1이 차이를 나타내고 이를 7로 나눈 나머지에 따라 요일을 출력하면 된다. 
'''
def get_day_of_week(month, day):
    '''
    2007년의 월, 일을 받아 요일을 반환하는 함수 
    
    Args:
        month(int): 월
        day(int): 일 
    Returns:
        str : 요일 
    '''
    day_max = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    num_days = 0 
    for i in range(1, month):
        num_days += day_max[i]
    num_days += day

    return day_of_week[(num_days - 1) % 7]

if __name__ == '__main__':
    input = sys.stdin.readline
    x, y = map(int, input().split())
    print(get_day_of_week(x, y))