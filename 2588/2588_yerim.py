a = int(input())
b = int(input())

c = a * int(b%10)
d = a * int((b%100)/10)
e = a * int(b/100)

print(c)
print(d)
print(e)
print(c+d*10+e*100)