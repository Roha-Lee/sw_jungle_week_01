n = int(input())

for i in range(n):
    num, letter = input().split()
    text = ''
    for i in letter:
        text = i * int(num)
        print(text, end='')
    print("\n", end="")