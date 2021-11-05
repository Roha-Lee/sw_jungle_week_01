import sys 
def find_spy(heights):
    total_heights = sum(heights)
    
    for first in range(8):
        for second in range(first+1, 9):
            if total_heights - heights[first] - heights[second] == 100:
                return first, second


if __name__ == '__main__':
    input = sys.stdin.readline
    heights = sorted([int(input()) for _ in range(9)])
    spy = find_spy(heights)
    for i in range(9):
        if i not in spy:
            print(heights[i])