import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    words = sorted(list(set([input().rstrip() for _ in range(n)])))
    words = sorted(words, key = lambda x: len(x))
    
    for word in words:
        print(word)
    