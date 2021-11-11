import sys 
cnt = [0] * 10001
# 계수 정렬
# 시간제한이 빡빡하기 때문에 O(nlogn)보다 빠른 정렬인 O(n)정렬 알고리즘을 이용
# 각각의 숫자를 카운트 한 후 낮은 순서부터 출력
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    for i in range(n):
        cnt[int(input())] += 1
    

    for i in range(10001):
        if cnt[i] != 0:
            for _ in range(cnt[i]):
                print(i)