# 10까지 짝수의 합계
# i = 2+4+6+8+10...i+2
# i%2==0 짝수 판별
# sum = sum + i

i = 0
sum = 0
while i<10:
    i = i + 1
    if i%2==0:
        sum = sum + i
    print(f'i={i}, sum={sum}, {i}%2={i%2==0} {i}<10={i<10}')
print(sum)