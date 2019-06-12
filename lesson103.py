# 1부터 5까지의 합 구하기
# i <= 5 
# 선처리 : sum = sum + i
# 후증가 : i = i + 1

i = 2   # 1  
sum = 1 # 0
while i <= 5:
    print(f'i={i}, sum={sum}, {i}<5={i<5}')
    sum = sum + i
    i = i + 1

print(f'1부터 5까지 합계 : {sum}')