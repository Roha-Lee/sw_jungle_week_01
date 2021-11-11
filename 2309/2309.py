import sys 
if __name__ == '__main__':
    input = sys.stdin.readline

    talls = []
    sum = 0
    for i in range(9):
        tall = int(input())
        talls.append(tall)
        sum += tall
    flg = False
    for i in range(8):
        for j in range(i+1, 9):
            if sum - (talls[i] + talls[j]) != 100:
                continue
            else:
                talls.pop(j)
                talls.pop(i)
                flg = True
                break
        if flg: 
            break

    talls.sort()
    for tall in talls:
        print(tall)