from pprint import pprint

# 행고정 열변화 직각 삼각형
# 데이터 유형 추적
# row=1  col= , , , ,5(2)
# row=2, col= , , ,4(3),5(5)
# row=3, col= , ,3(7),4(11),5(13)
# row=4, col= ,2(17),3(19),4(23),5(29)
# row=5, col=1(31),2(37),3(41),4(43),5(47)
# row=0,5,1
# col=4-row,5,1

num = list(range(2,101))
for i in range(2,101):
    for j in range(2,101):
        if i <= j:
            break
        if i%j == 0:
            num.remove(i)
            break

cnt=0
arr = [[0]*5 for x in range(5)] 
for row in range(0,5,1):
    for col in range(4-row,5,1):
        arr[row][col] = num[cnt]
        cnt = cnt + 1
pprint(arr)