# 효율적인 알고리즘 설계하기



# 일반적인 코드 실행 시간 측정하기
from timeit import default_timer as timer
before = timer()
cnt = 0
for i in range(1,100):
    if check_prime(i):
        cnt = cnt + 1
print(cnt)
after = timer()
print(after - before)

# 개선된 알고리즘 시간 측정하기
import math
before = timer()
def check_prime(n):
    flag = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def cnt_prime(a,b):
    cnt = 0
    for i in range(a,b):
        if check_prime(i):
            cnt = cnt + 1
    return cnt

print(cnt_prime(1,100))
after = timer()
print(after - before)
