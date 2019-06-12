# 1부터 5까지의 합 구하기
# i < 5 
# 선증가 : i = i + 1
# 후처리 : sum = sum + i

i = 1  
sum = 1
while i < 5:
    i = i + 1
    sum = sum + i
    print(f'i={i}, sum={sum}, {i}<5={i<5}')

print(f'1부터 5까지 합계 : {sum}')