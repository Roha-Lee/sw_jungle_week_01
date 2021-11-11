n = int(input())

nums = []
words = []

for i in range(n):
    k, string = input().split()

    nums.append(int(k))
    words.append(list(string))

for i in range(n):      # 각 입력의 개수만큼 반복
    for j in range(len(words[i])):       # 입력받은 string의 길이만큼 반복
        for k in range(nums[i]):      # 반복해야 하는 횟수만큼 반복
            print(words[i][j], end="")
    print("\n", end="")