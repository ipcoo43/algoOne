# 홀수 마방진

n = 5  # 홀수 개수만 입력
arr = [[0]*n for x in range(n)] # 배열 생성 초기화

# 시작을 위한 위치 설정
row = 0  
col = n//2
arr[row][col] = 1 # 시작 위치에 1을 넣고 시작

# 행의 오른쪽 끝 열의 상단 끝에 있을 경우 되돌아오기 위해 위치 넣을 변수
x = 0
y = 0

for i in range(2,n*n+1):
    x = row  
    y = col
    
    row = row - 1 # 행 감소
    col = col + 1 # 열 증가
    
    if row < 0:      # 행이 0보다 작으면
        row = n - 1  # 행은 n에서 1 감소로 이동
    
    if col > n-1 :   # 열이 n-1 보다 크면
        col = 0      # 열은 0으로 이동
    
    if arr[row][col] == 0: # 배열의 값이 0이면  
        arr[row][col] = i  # i를 배열에 저장 한다
    else:                  # 그렇지 않으면
        row = x + 1        # x+1의 값을 행에 저장하고
        col = y            # y를 열에 저장하고
        arr[row][col] = i  # i를 배열에 저장 한다

for row in range(0,n):
    for col in range(0,n):
        print(f'{arr[row][col]:2d}',end=' ')
    print()