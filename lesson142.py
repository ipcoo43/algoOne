# 소수 판별 문제

# 소수 여부 판별하기
n=10237
flag = True

for i in range(2,n):
    if n % i == 0:
        flag = False
if flag:
    print('prime number')
else:
    print('not prime number')

# 소수 여부 판별하는 함수
def check_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
if check_prime(171):
    print('prime number')
else:
    print('not prime number')

# 소수 여부 판별하는 함수의 활용
for i in range(1,11):
    print(i, check_prime(i))

for i in range(1,11):
    if check_prime(i):
        print(i,end=' ')
