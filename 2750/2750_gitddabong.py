import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numbers = []

    for i in range(n):
        numbers.append(int(input()))

    numbers.sort()
    for number in numbers:
        print(number)