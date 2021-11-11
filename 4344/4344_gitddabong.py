n = int(input())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

for group in array:
    del group[0]
    sum_grade = sum(group)
    length = len(group)
    avg = sum_grade / length

    count = 0
    for person in group:
        if avg < person:
            count += 1

    percent = count / length * 100

    print(f"{percent:.3f}" + "%")
    