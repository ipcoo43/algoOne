# 배수 구하기
# 배수 로직 : 그 수를 를 나눠 떨어지느냐 ( 나머지가 0 이다)
# 2의 배수 : i % 2 == 0
# 3의 배수 : i % 3 == 0 
# 4의 배수 : i % 4 == 0 
# 5의 배수 : i % 5 == 0 

# < 문제 > 1부터 100까지의 5의 배수의 개수와 합 구하기

cnt = 0
sum = 0

for i in range(1,101):
    mok = i//5
    rem = i - mok*5
    if rem == 0:
        cnt = cnt + 1
        sum = sum + i

print(f'cnt={cnt}, sum={sum}')
