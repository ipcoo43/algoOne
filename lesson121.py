# 에라토스체

def is_prime(num):
    if num <=1 :
        return False
    i = 2
    while i*i <= num:
        if num%i ==0:
            return False
        i = i + 1
    return True

print(is_prime(11))