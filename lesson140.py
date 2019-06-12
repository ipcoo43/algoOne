# 함수의 기초

# 1+2 출력하기
a=1
b=2
print(a+b)

# 1+2 출력하는 함수
def add():
    a = 1
    b = 2
    print(a+b)
add()

# a+b를 출력하는 함수
def addOne(a,b):
    print(a+b)
addOne(1,2)

# a+b를 돌려주는(return) 함수
def addTwo(a,b):
    return a+b
print(addTwo(1,2))
print(addTwo(addTwo(1,2),addTwo(1,2)))