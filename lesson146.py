# 에라토스테네스의 체
# 1) n까지의 체를 만든다
# 2) 소수를 저장할 저장공간(리스트)을 만든다.
# 3) 체의 첫 번째 숫자, 2(i)를 저장 한다.
# 4) 체에서 2(i)의 배수를 지운다
# 5) n까지 3) 4)를 반복한다.

# for 반복문 사용
def eratosOne(n):
    sieve = [1] * (n + 1) # n까지의 1를 원소로하는 체를 만든다
    prime = [] # 소수를 저장할 리스트 생성
    for i in range(2, n+1): # 체에 걸러 낼 숫자 2부터 n+1까지원소 i에 대해
        if sieve[i] == 1:   # 체 리스트[i] 원소가 1과 같다면
            prime.append(i) # prime에 i를 저장하고
            for j in range(i,n+1,i): # i부터 n+1까지 i씩의 원소의 j에 대한
                                     # range(i,n+1,i) 배수
                sieve[j] = 0 # 체의 리스트[j]에 0을 저장 한다
    return prime
print(eratosOne(12))

# for 반복문 범위 나누기
def eratosTwo(n):
    sieve = [1]*(n+1)
    prime = []
    for i in range(2,int(n**0.5)+1):
        if sieve[i] == 1:
            prime.append(i)
            for j in range(i, n+1, i):
                sieve[j] = 0
    for i in range(int(n**0.5)+1, n+1):
        if sieve[i] == 1:
            prime.append(i)
    return prime
print(eratosTwo(12))

# 먼저 체크만하고 한꺼번에 담기
def eratosThree(n):
    sieve = [1] * (n+1)
    prime = []
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == 1:
            for j in range(i+i, n+1, i):
                sieve[j] = 0
    