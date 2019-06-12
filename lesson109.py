# 2! + 3! + 4! + 5!
# i : 1씩 증가되는 숫자를 저장하기 위한 변수
# f : 각 항을 저장하기 위한 변수
# sum : 합계를 저장하기 위한 변수

i = 1
f = 1
sum = 0

while i<5:
    i = i + 1
    f = f * i
    sum = sum + f
    print(f' i={i}, f={f}, sum={sum}')

print('result :', sum)