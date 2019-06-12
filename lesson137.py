# 마방진

n = 3
arr = [[0]*n for x in range(n)]

row = 1
col = (n+1)//2

k = 1
arr[row-1][col-1] = k

while k < n*n:
    k = k + 1
    if k%n==1:
        col = col - 1
    else:
        row = row - 1
        col = col - 1
        if row < 1:
            row = n
        if col < 1:
            col = n
        arr[row-1][col-1] = k

for i in range(n):
    print(arr[i])