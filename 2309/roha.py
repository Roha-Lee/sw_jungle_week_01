import sys 
def find_spy(heights):
    total_heights = sum(heights)
    # 전체 9명의 난쟁이들의 키의 합을 구한 후 
    for first in range(8):
        for second in range(first+1, 9):
            # 두명을 뽑아서 전체키 - 두명키의 합을 통해 7명의 키의 합을 구함 
            # 100인경우 리턴
            if total_heights - heights[first] - heights[second] == 100:
                return first, second


if __name__ == '__main__':
    input = sys.stdin.readline
    heights = sorted([int(input()) for _ in range(9)])
    spy = find_spy(heights)
    for i in range(9):
        if i not in spy:
            print(heights[i])