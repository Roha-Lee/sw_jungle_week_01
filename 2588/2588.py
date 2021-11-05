n = int(input())
m = int(input())

# n은 건드릴 필요가 없으니 m만 각각의 자리수만 남기기
m100 = int(m / 100)
m10 = int((m - m100 * 100) / 10)
m1 = m % 10

result1 = n * m1
result2 = n * m10
result3 = n * m100

print(result1)
print(result2)
print(result3)

sum = result1 + result2 * 10 + result3 * 100
print(sum)