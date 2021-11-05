x, y, w, h = map(int, input().split())

a = w - x
b = y
c = x
d = h - y

print(min(a, b, c, d))