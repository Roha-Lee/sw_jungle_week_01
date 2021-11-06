import sys 
def gen_repeat_str(n, query):
    # 빈 스트링으로 결과 초기화
    result = ''
    for letter in query:
        # query의 각각의 letter를 스캔하면서 빈 스트링에 letter * n을 더해줌 A -> AAAA (if n=4)
        result += letter * n
    return result
if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        n, query = input().split()
        n = int(n)
        print(gen_repeat_str(n, query))