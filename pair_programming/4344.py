import sys
n = int(sys.stdin.readline())

# n명의 학생 수와 각각의 점수가 주어짐
# 이 점수로 평균을 만들고
# 이 평균보다 점수가 높은사람의 비율을 출력

scores = []
for i in range(n):
    scores.append(list(map(int, sys.stdin.readline().split())))
    scores[i].pop(0)

for i in range(n):
    scores_sum = sum(scores[i])
    avg = scores_sum / len(scores[i])
    
    count = 0
    for person in scores[i]:
        if person > avg:
            count += 1
        else:
            continue

    percent = count / len(scores[i]) * 100
    print(f'{round(percent, 3):.3f}%')