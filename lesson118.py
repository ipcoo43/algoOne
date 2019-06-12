# 소수(素數, Prime Number) 구하기

num = 7
j = 2
# for j in range(2,num+1):
while j <= num:
    if num % j == 0:
        if num == j:
            print('prime')
            break
        else:
            print('no prime')
            break
    j = j + 1
    