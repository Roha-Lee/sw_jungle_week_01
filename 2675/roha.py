import sys 
def gen_repeat_str(n, query):
    result = ''
    for letter in query:
        result += letter * n
    return result
if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        n, query = input().split()
        n = int(n)
        print(gen_repeat_str(n, query))