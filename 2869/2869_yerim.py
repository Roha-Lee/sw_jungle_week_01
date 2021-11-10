a, b, v = map(int, input().split())

#낮에 a미터 올라감, 밤에 b미터 내려감, 정상에선 안미끄러짐
#v미터 다 올라가려면 며칠(count)?

day = 0
tree = 0

while True:
    day += 1
    tree += a
    if tree >= v:
        print(day)
        break
    tree -= b 