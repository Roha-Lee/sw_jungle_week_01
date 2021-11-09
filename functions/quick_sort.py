import sys
input = sys.stdin.readline

# left, right가 왜 있냐?
# 재귀로 돌릴 예정이고 이 알고리즘에서는 리스트를 계속해서 재귀로 분할할 예정이기 때문에.
def qsort(list, left, right):
    pl = left
    pr = right
    pivot = list[(left + right) // 2]

    # 피벗이 서로 만나면 종료
    while pl <= pr:
        # 피벗보다 큰 원소를 피벗 기준 왼쪽에서 찾기
        while list[pl] < pivot:
            pl += 1
        # 피벗보다 작은 원소를 피벗 기준 오른쪽에서 찾기
        while list[pr] > pivot:
            pr -= 1
        # pl은 피벗 왼쪽에, pr은 피벗 오른쪽에 위치할 때
        if pl <= pr:
            # 서로 수를 스왑
            list[pl], list[pr] = list[pr], list[pl]
            # 왼쪽 오른쪽 포인터 옮기기
            pl += 1
            pr -= 1

    if left < pr:
        qsort(list, left, pr)
    if pl < right:
        qsort(list, pl, right)


def quick_sort(list):
    qsort(list, 0, len(list) - 1)

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    
    quick_sort(numbers)
    print(numbers)
