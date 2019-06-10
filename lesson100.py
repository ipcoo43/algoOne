# 1부터 5까지의 합 구하기
# i < 5
# 선증가 : i=i+1
# 후처리 : sum=sum+i

i=0
sum=0
while i < 5:
    i = i + 1
    sum = sum + i
    print(f'i={i} 일때 sum={sum}')

print('1부터 5까지 합계 :',sum)