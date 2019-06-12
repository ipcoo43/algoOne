# 분수 수열의 합계 (스위치 변수)
# 분수 수열 문제의 해법
# 분자, 분모의 상호 연관성 확인
# 연과성이 없을 때는 분자, 분모의 반복 규칙을 따로 찾자
# 분자, 분모의 변수 중 어느것으로  종료 할 것인가

# 1/2+2/3+3/4+4/5 ... i/i+1
# 분자 : i = i + 1
# 분모 : i/(i+1)
# sum = sum + i/(i+1)
# i < 4

from fractions import Fraction
i = 0    # 1
sum = 0  # 1/2
while i < 4:
    i = i + 1
    n = Fraction(i,i+1)
    sum = sum + n
    print(f'i={i}, n={n}, sum = {sum}')

print(f'result : {sum}')
print(163/60)
print()

i = 0    # 1
sum = 0  # 1/2
while i < 4:
    i = i + 1
    n = i/(i+1)
    sum = sum + n
    print(f'i={i}, n={n}, sum = {sum}')

print(f'result : {sum}')
