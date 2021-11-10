a = int(input())
b = int(input())

c = a * int(b%10) # a * b를 10으로 나눈 나머지(셋째자리)
d = a * int((b%100)/10) # a * b를 100으로 나눈 나머지에 10으로 나눔 
e = a * int(b/100) # a * b를 100으로 나눈 값(첫째자리)

print(c)
print(d)
print(e)
print(c+d*10+e*100)