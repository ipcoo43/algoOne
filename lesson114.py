# 분수 수열의 합계 (스위치 변수)
# 1/2+2/3+3/4+4/5 ... i/i+1
# 분자 : i = i + 1
# 분모 : i/(i+1)
# sum = sum + i/(i+1)
# i < 4
# from fractions import Fraction

a = 1
b = 2
sum = 0
while a<=4:
    sum = sum + (a/b)
    a = a + 1
    b = b + 1

print(f'sum = {sum:.2f}')