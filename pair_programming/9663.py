import sys 

# def n_queen(n, start = 0):
#     global count

#     if start == n: 
#         count += 1
#         return 
#     # [0, 1, 2, 3]
#     for i in range(n):
#         # False 갈 수 있음 True 갈 수 없음
#         if not flag_a[i] and not flag_b[start - i + n - 1] and not flag_c[start + i]:
#             flag_a[i] = True 
#             flag_b[start - i + n - 1] = True
#             flag_c[start+i] = True
#             n_queen(n, start + 1)
#             flag_a[i] = False
#             flag_b[start - i + n - 1] = False
#             flag_c[start+i] = False

def n_queen_local(n, flag_a, flag_b, flag_c, start = 0, count = 0):
    if start == n: 
        return count + 1
    
    for i in range(n):
        if not flag_a[i] and not flag_b[start - i + n - 1] and not flag_c[start + i]:
            flag_a[i] = True 
            flag_b[start - i + n - 1] = True
            flag_c[start+i] = True
            count = n_queen_local(n, flag_a, flag_b, flag_c, start + 1, count)
            # count = 1
            flag_a[i] = False
            flag_b[start - i + n - 1] = False
            flag_c[start+i] = False
    
    return count 
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())    
    
    count = 0 
    flag_a = [False] * n
    flag_b = [False] * (2 * (n-1) + 1)
    flag_c = [False] * (2 * (n-1) + 1)

    # n_queen(n)
    # print(count)
    print(n_queen_local(n, flag_a, flag_b, flag_c))