# flowchart for python code
# please enter the value : 값을 입력하시오
# Invalid Input! : 잘못된 입력!
# Enter numeric data :  숫자 데이터 입력
# Enter value between 0 and 100 : 0에서 100 사이의 값을 입력하시오

def get_value():
    while True:
        try:
            value = int(input('please enter the value: '))
        except ValueError:
            print('Error : Invalid Input! Enter numeric data.\n')
            continue
        if (value < 1 or value > 100):
            print('Error : Invalid Input! Enter value between 0 and 100\n')
        else:
            break
    return value

# get_value
# while True : 순환 루프 아래로 이동
# prease enter the value : 입력 아래로 이동
# ValueErro  : 조건 판단
#   Yes - Error : Invalid Input! Enter numeric data
#   No  - 아래로 이동
# value < 1 or value > 100 : 조건 판단
#   Yes - Error : Invalid Input! Enter value between 0 and 100
#   No  - 아래로 이동
# Return value    