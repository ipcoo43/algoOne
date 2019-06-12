# 에라토스체

num = list(range(2,101))
for i in range(2,101):
    for j in range(2,101):
        if i <= j:
            break
        if i%j == 0:
            num.remove(i)
            break
print(num)