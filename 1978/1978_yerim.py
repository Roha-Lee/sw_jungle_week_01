n = int(input())
nums = list(map(int,input().split()))
sosu_count = 0

for i in nums :
    count = 0
    if i == 1 : # 1이면 소수가 아니니 지나간다
        continue
    
    for j in range(2, i+1) : #2로 나눠보고 3으로도 나눠보고..
        if i % j == 0: #나머지가 0이면 소수. (1과 자기자신 이외로 나뉘어지면 안되니까)
            count += 1
    if(count == 1) : #약수가 1개여야 소수니까
        sosu_count += 1
print(sosu_count)