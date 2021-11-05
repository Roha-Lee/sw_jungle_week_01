import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    # 단어를 문제의 조건에 맞게 정렬하려면 먼저 사전 순서대로 정렬해주고 길이순으로 정렬하면 된다. 
    # 이게 가능한 이유는 파이썬은 정렬안정성을 보장하기 때문이다. 
    words = sorted(list(set([input().rstrip() for _ in range(n)])))
    words = sorted(words, key = lambda x: len(x))
    
    for word in words:
        print(word)
    