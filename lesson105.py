# 10까지 짝수의 합계
# i = 2+4+6+8+10...i+2
# sum = sum + i

print('선증가')
i=0
sum=0
while i < 10:
    i = i + 2
    sum = sum + i
    print(f'i={i}, sum={sum}, i<10={i<10}')

print(f'1부터 10까지 짝수의 합계 : {sum}')
print()

print('후증가')
i=4
sum=2
while i <= 10:
    sum = sum + i
    i = i + 2
    print(f'i={i}, sum={sum}, i<10={i<10}')

print(f'1부터 10까지 짝수의 합계 : {sum}')    