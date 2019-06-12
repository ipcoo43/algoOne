# 열고정 행변화
from pprint import pprint 

arr = [[0]*5 for x in range(5)]
k = 0
for col in range(5):
    for row in range(5):
        k = k + 1
        arr[row][col] = k
pprint(arr)