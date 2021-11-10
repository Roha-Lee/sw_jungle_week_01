import sys 

if __name__ == "__main__":
    input = sys.stdin.readline
    width, height = map(int, input().split())
    num_cut = int(input())

    h_list = [height] #23번 주석 내용 참고
    v_list = [width]
    for _ in range(num_cut):
        # 가로인지 세로인지, 가로세로의 위치(번호)
        vh, location = map(int, input().split()) 
        if vh == 0:
            h_list.append(location)
        else:
            v_list.append(location)

    # 정렬
    h_list.sort()
    v_list.sort()

    # 첫 도형의 높이
    h_max = h_list[0] #다른 코드들처럼 처음에 [0,x]를 안넣고
    v_max = v_list[0] #첫값을 밑에서 h_max로 고정 후 차를 계산

    # 리스트 내부에 있는 길이들의 차의 최댓값 구하기
    for i in range(len(h_list) - 1):
        h_max = max(h_max, h_list[i+1] - h_list[i])
    
    # 리스트 내부에 있는 길이들의 차의 최댓값 구하기
    for i in range(len(v_list) - 1):
        v_max = max(v_max, v_list[i+1] - v_list[i])
        
    #가로, 세로를 따로 계산하기때문에 다른 코드보다 빠름
    
    print(v_max * h_max)