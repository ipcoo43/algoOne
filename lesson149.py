# 나눗셈

arr = list(map(int, input('>>> ').strip().split(' ')))
a = arr[0]
b = arr[1]
res = round(a/b,10)
print('result :',res)