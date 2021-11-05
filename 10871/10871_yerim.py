n, x  = map(int, input().split())

num = list(map(int, input().split()))

for i in num :
    if i < x:
        print(i)

# n개가 들어있는 수열 a에서 정수x보다 작은 숫자 모두 출력
