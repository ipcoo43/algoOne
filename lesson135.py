# 홀수 마방진

from pprint import pprint

arr = [[0]*5 for x in range(5)]

arr[0][2]=1
arr[4][3]=2
arr[3][4]=3
arr[2][0]=4
arr[1][1]=5
arr[2][1]=6
arr[1][2]=7
arr[0][3]=8
arr[4][4]=9
arr[3][0]=10
arr[4][0]=11
arr[3][1]=12
arr[2][2]=13
arr[1][3]=14
arr[0][4]=15
arr[1][4]=16
arr[0][0]=17
arr[4][1]=18
arr[3][2]=19
arr[2][3]=20
arr[3][3]=21
arr[2][4]=22
arr[1][0]=23
arr[0][1]=24
arr[4][2]=25

pprint(arr)