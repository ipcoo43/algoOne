from pprint import pprint

# 행고정 열변화 직각 삼각형
# 데이터 유형 추적
# row=1  col= , , , ,5
# row=2, col= , , ,4,5
# row=3, col= , ,3,4,5
# row=4, col= ,2,3,4,5
# row=5, col=1,2,3,4,5
# row=0,5,1
# col=4-row,5,1

arr = [[0]*5 for x in range(5)]
k=0
for row in range(0,5,1):
    for col in range(4-row,5,1):
        k = k + 1
        arr[row][col] = k
pprint(arr)