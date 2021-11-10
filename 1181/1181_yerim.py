import sys
n = sys.stdin.readline()

words = []
for i in range(n):
    words.append(sys.stdin.readline().strip())
    
result = words.sort()
print(result)