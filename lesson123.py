# 기본 5행 5열(2차원 배열)
# (행, 열)
# 행고정 열변화 : 가로 방향 입력
# 열고정 행변화 : 세로 방향 입력

print('행고정 열변화')
arr=[[0]*5 for x in range(5)]
k=0
for row in range(5):     # 행고정 
    for col in range(5): # 열변화
        k = k + 1
        arr[row][col] = k
print(arr)
print()

print('열고정 행변화')
arr=[[0]*5 for x in range(5)]
k=0
for col in range(5):     # 열고정 
    for row in range(5): # 행변화
        k = k + 1
        arr[row][col] = k
print(arr)