# 1/2 - 2/3 + 3/4 - 4/5 ... i/(i+1)
# sum : 계산 결과 누적 변수
# i   : 계산식의 수를 증가 시키기 위한 변수
# sw  : 부호를 판단하기 위한 변수
# 스위치 변수 : on, off

i = 0
sum = 0
sw = 0
while i < 4:
    i = i + 1
    if sw == 0:
        sum = sum + (i/(i+1))
        sum = 1
    else:
        sum = sum - (i/(i+1))
        sum = 0

print(f'sum={sum:.2f}')