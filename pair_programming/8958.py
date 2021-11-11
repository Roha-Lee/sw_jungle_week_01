import sys 
def get_score(user_input):
    total_score = 0
    score = 0            
    for letter in user_input:
        if letter == "O":
            score += 1
            total_score += score
        else:
            score = 0
    return total_score        

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        user_input = input().rstrip()
        score = get_score(user_input)
        print(score)

