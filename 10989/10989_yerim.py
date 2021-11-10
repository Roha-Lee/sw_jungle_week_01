#도수정렬(=계수정렬) p.297
n = int(input())

#주어질 자연수 0부터 10,000까지니까 인덱스[0]을 10001개
count = [0] * 10001 

#input_num와 count[]의 i(인덱스숫자)가 일치하면 +1씩 카운팅
for i in range(n):
    input_num = int(input())
    count[input_num] += 1 

#1이 몇개 인지 ~ 10001까지 갯수 세본다
for number in range(10001): 
    #센 숫자가 0개이면 pass
    if count[number] == 0:
        continue
    else:
        #센 숫자가 있는 만큼 반복. 순서대로 세기 때문에 정렬코드 안써도 정렬이 됨
        for j in range(count[number]):
            print(number)
