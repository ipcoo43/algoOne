# 10개의 정수 중에서 홀수의 개수와 짝수의 개수 구하기
# i : 인덱스 변수(배열첨자 변수)
# arrary(10) : 배열 변수
# evenCnt : 짝수의 개수
# oddCnt : 홀수의 개수
# rem : 나머지 변수

array = [1,2,3,4,5,6,12,8,9,10]
i=0
evenCnt=0
oddCnt=0

while i < 10:
    if array[i] % 2 == 0:
        evenCnt = evenCnt + 1
    else:
        oddCnt = oddCnt + 1
    i = i + 1
    
print(f'짝수는 {evenCnt}개, 홀수는 {oddCnt}개')
    