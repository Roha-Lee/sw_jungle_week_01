import sys

def get_hansu_num(n):
    if n <= 99:
        hansu = n
    else:
        hansu = 99
        for i in range(100, n+1):
            num_list = list(map(int,str(i)))
            
            if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
                hansu += 1
    return hansu

if __name__ == "__main__":
    input_num = int(sys.stdin.readline())
    
    print(get_hansu_num(input_num))