# 소수 판별 - 시간 측정
from timeit import default_timer as timer

import math
before = timer()
def check_prime_one(n):
    flag = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
check_prime_one(11)
after = timer()
print(after - before)

before = timer()
def check_prime_two(n):
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
check_prime_two(11)
after = timer()
print(after - before)

# 소수 리스트 만들
def prime_list(n):
    prime = []
    for i in range(1,n):
        if check_prime_two(i):
            prime.append(i)
    return prime
print(prime_list(11))