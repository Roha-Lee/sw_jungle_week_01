import sys
input = sys.stdin.readline
write = sys.stdout.write

talls = []
sum = 0
for _ in range(9):
    n = int(input())
    talls.append(n)
    sum += n

# 리스트의 두 수를 더한 값이 target이면, 그 두 수를 제외한 모든 난쟁이가 진짜 일곱난쟁이
target = sum - 100

i = 0
while True:
    if len(talls) == 7:
        break

    for j in range(i+1, 9):
        left = talls[i]
        right = talls[j]
        pair = left + right
        if pair == target:
            talls.remove(left)
            talls.remove(right)
            break
    
    i += 1

talls.sort()
for tall in talls:
    print(tall)