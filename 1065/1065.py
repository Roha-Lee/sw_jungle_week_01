import sys

n = int(sys.stdin.readline())

count = 0
for i in range(1,n):
    # 세자리 수가 안되는 수는 모두 한수로 쳐주더라
    if i < 100:
        count += 1
        continue

    # 수를 자릿수대로 나누기
    i100 = int(i / 100)
    i10 = int((i - i100 * 100) / 10)
    i1 = i % 10

    if i100 - i10 == i10 - i1:
        count += 1
    else:
        continue

print(count)