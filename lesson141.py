# 자연수 n의 약수를 출력하는 함수

# 일반적인 코드로 작성하기
n = int(input('n을 입력해주세요 : '))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# 입력이 없는 함수로 작성하기
def divisor():
    n = int(input('n을 입력해주세요 : '))
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
divisor()

# 입력이 있는 함수로 작성하기
def divisorOne(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
divisorOne(6)
print()

for i in range(6,12,24):
    divisorOne(i)