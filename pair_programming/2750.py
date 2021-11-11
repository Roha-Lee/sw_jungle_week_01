import sys 

def insertion_sort_1(nums):
    n = len(nums)
    for i in range(1, n):
        loc = 0
        for j in range(i):
            if nums[j] < nums[i]:
                loc += 1
            else:
                break
        nums.insert(loc, nums.pop(i))
    return nums

def insertion_sort_2(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break

    return nums

if __name__ == '__main__':
    input = sys.stdin.readline
    time_1 = 0
    time_2 = 0 
    
    insertion_sort_1([1,2,3,4,5])
    insertion_sort_2([1,2,3,4,5])
    