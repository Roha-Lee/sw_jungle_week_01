import sys 
def escape_rectangle(x, y, w, h):
    return min(x, y, w-x, h-y)
if __name__ == '__main__':
    input = sys.stdin.readline
    x, y, w, h = map(int, input().split())
    print(escape_rectangle(x, y, w, h))