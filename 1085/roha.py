import sys 
def escape_rectangle(x, y, w, h):
    # 사각형을 빠져나오려면 아래 4개의 값중 최소값(직선 거리)을 찾으면 된다. 
    return min(x, y, w-x, h-y)
if __name__ == '__main__':
    input = sys.stdin.readline
    x, y, w, h = map(int, input().split())
    print(escape_rectangle(x, y, w, h))