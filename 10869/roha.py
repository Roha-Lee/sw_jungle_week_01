import sys 
import operator
input = sys.stdin.readline
A, B = map(int, input().split())
# operator를 함수로 사용할 수 있도록 operator모듈에서 각각에 해당하는 함수를 얻어 온다. 
op_list = [operator.add, operator.sub, operator.mul, operator.floordiv, operator.mod]
# 연산을 수행하여 값을 출력한다. 
for op in op_list:
    print(op(A, B))