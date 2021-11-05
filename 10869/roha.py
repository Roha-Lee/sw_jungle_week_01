import sys 
import operator
input = sys.stdin.readline
A, B = map(int, input().split())
op_list = [operator.add, operator.sub, operator.mul, operator.floordiv, operator.mod]
for op in op_list:
    print(op(A, B))