import sys
n = int(sys.stdin.readline())

scores = []

for i in range(n):
    scores.append(list(map(int, sys.stdin.readline().split())))
    scores[i].pop(0)

#학생들 점수 평균
for i in scores:
    scores_sum = sum(scores[i])
    avg = scores_sum / len(scores[i])

#평균을 넘는 학생들의 비율
    count = 0
    for person in scores[i]:
        if person > avg:
            count += 1
#몇 명 중 몇 명? (비율)
    rate = count / len(scores[i]) * 100
    #비율을 반올림하여 소수점 셋째 자리까지 출력
    print(f'{round(rate,3):.3f}%')
