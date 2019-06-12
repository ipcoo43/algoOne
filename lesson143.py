# 소수 카운트


# 소수 여부 판별 함수
def check_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# 소수 카운트하기
cnt = 0
for i in range(1,100):
    if check_prime(i):
        cnt = cnt + 1
print(cnt)

# 소수 카운트 함수
def cnt_prime(a,b):
    cnt = 0
    for i in range(a,b):
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag = False
            break
        if flag:
            cnt = cnt + 1
    return cnt
print(cnt_prime(2,4))

# 소수 판별 함수를 사용하는 소수 카운트 함수
def cnt_prime_check(a,b):
    cnt = 0
    for i in range(a,b):
        if check_prime(i):
            cnt = cnt + 1
    return cnt
print(cnt_prime_check(2,4))