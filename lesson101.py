# 1부터 5까지의 합 구하기
# i <= 5 , i < 6
# 선처리 : sum = sum + i
# 후증가 : i = i + 1


i = 0
sum = 0
while i <= 5:
    sum = sum + i
    i = i + 1
    print(f'i={i} 일때 sum={sum}')

print(f'1부터 5까지 합계 : {sum}')