# 기본 5행 5열(2차원 배열)
# 행고정 열변화
from pprint import pprint

arr=[[0]*5 for x in range(5)]
k = 0
for row in range(5):
    for col in range(5):
        k = k + 1
        arr[row][col] = k

pprint(arr)