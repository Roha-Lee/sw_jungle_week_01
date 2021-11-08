n = int(input())


for i in range(n):
    num = input()
    total_score = 0
    score = 0 
    for ox in num:
        if ox == 'O':
            score += 1
            total_score += score
        elif ox == 'X':
            score = 0
    print(total_score)

    