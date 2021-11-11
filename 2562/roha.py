def find_max(nums):
    max_elem = 0
    pos = -1
    # 최대값과 그 위치를 스캔하면서 찾아서 반환
    for i, num in enumerate(nums):
        if num > max_elem: 
            max_elem = num
            pos = i + 1
    return pos, max_elem
if __name__ == '__main__':
    nums = [int(input()) for _ in range(9)]
    pos, max_val = find_max(nums)
    print(max_val)
    print(pos)
