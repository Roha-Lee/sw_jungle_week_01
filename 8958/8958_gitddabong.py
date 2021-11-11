n = int(input())
array = []
for i in range(n):
    array.append(list(input()))     # 문자열을 list로 감싸면 한 글자씩 쪼갠 하나의 리스트로 만들 수 있다

for i in range(n):
    win_rate = 0
    sum = 0
    for result in array[i]:
        if result == "O":
            win_rate += 1
            sum += win_rate
        else:
            win_rate = 0

    print(sum)