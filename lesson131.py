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

prm = [x*0 for x in range(15)] # 배열의 초기 값
prm[0] = 2 # 0번지에 2를 입력
prm[1] = 3 # 1번지에 3을 입력
cnt = 1    # 2번지 부터 입력됩
for p in range(5,101,2): # 5,7,9,11, 짝수 값은 제외 시킴
    for q in range(1,cnt): 
        mok = p//prm[q]      # p/prm[1] = 5/3
        nam = p-(mok*prm[q]) # 
        if nam == 0: # p%prm[q]
            break
    cnt = cnt + 1
    prm[cnt] = p
    if cnt == 14:
        break

cnt=0
arr = [[0]*5 for x in range(5)] 
for row in range(0,5,1):
    for col in range(4-row,5,1):
        arr[row][col] = prm[cnt]
        cnt = cnt + 1
pprint(arr)