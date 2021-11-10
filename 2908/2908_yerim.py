a, b = input().split()

A = a[::-1]
B = b[::-1]

# 이게 문자열 비교라는거 알고있었니? -> 사전순 비교
if A > B:
    print(A)
else:
    print(B)