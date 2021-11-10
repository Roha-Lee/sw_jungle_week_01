# -*- coding: utf-8 -*-
import sys 

def sort_standard(element):
    return len(element)

if __name__ == '__main__':
    input = sys.stdin.readline 
    n = int(input())
    # words = []
    words = set()

    for _ in range(n):
        user_input = input().rstrip()
        words.add(user_input) # O(1)
    
    
    words = list(words)
    words = sorted(words)
    words = sorted(words, key = lambda x: len(x))
    # 정렬 안정성
    # ['ape','apple','wait','wont']
    # 길이순서 
    # ['ape','wont', 'wait','apple']
    # 사전순서 
    # ['ape','apple','wait', 'wont']
    print(words)
    
    # 길이가 짧은 것부터 
    # 길이가 같으면 사전 순으로 


    # # 리스트 컴프리헨션 
    # [ x 
    #     for x in range(3, 10)
    # ] # -> [3,4,5,6,7,8,9]

    # words = [input().rstrip() for _ in range(n)]