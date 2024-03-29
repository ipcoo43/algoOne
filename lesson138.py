# 대각선 채우기

# 1회전 : 1 
# 2회전 : 2,3
# 3회전 : 4,5,6
# 4회전 : 7,8,9,10
# 5회전 : 11,12,13,14,15
# 6회전 : 16,17,18,19
# 7회전 : 20,21,22
# 8회전 : 23,24
# 9회전 : 25

# 행고정, 열변화, 열고정 행변화 인지 판별 : 아니다
# 2차원 배열은 배열 순서를 적으면 규칙을 찾을 수 있다.
# 순서쌍을 더하면 0 ~ 8 까지의 규칙을 찾을 수 있다.
# 1회전 : (0,0) 0
# 2회전 : (0,1),(1,0) 1 
# 3회전 : (0,2),(1,1),(2,0) 2
# 4회전 : (0,3),(1,2),(2,1),(3,0) 3
# 5회전 : (0,4),(1,3),(2,2),(3,1),(4,0) 4
# 6회전 : (1,4),(2,3),(3,2),(4,1) 5
# 7회전 : (2,4),(3,3),(4,2) 6
# 8회전 : (3,4),(4,3) 7
# 9회전 : (4,4) 8

# 행 + 열 = 회전
from pprint import pprint

arr = [[0]*5 for x in range(5)]
k = 0
for row in range(0,9):
    for col in range(5):
        j = row - col
        if j < 0:
            break
        if j > 4:
            break
        k = k + 1
        arr[row][col] = k

pprint(arr)