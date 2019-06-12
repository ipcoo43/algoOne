# 1부터 5까지 반복 구조

sum = 0
for i in range(1,6,1):
    sum = sum + i
    print(f'i={i}, sum={sum}, {i}<6={i<6}')

print(f'1부터 5까지 sum의 합계 = {sum}')