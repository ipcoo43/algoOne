from pprint import pprint

arr = [[0]*5 for x in range(5)]
k = 0
row = 0
while row<5:
    col = 0
    while col<5:
        k = k + 1
        arr[row][col] = k
        col = col + 1
    row = row + 1
pprint(arr)
        