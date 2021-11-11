import sys
input = sys.stdin.readline
write = sys.stdout.write

testcase = int(input())

# 인덱스는 문자열의 길이를 뜻함
li = [[] for _ in range(51)] 
for i in range(testcase):
    text = input().rstrip('\n')
    t_len = len(text)

    # 넣을 텍스트가 이미 존재하면 넘어가기
    if text in li[t_len]:
        continue
    else:
        li[t_len].append(text)

for i in range(len(li)):
    if len(li[i]) == 0:
        continue
    li[i].sort()
    for text in li[i]:
        write(text + "\n")
    