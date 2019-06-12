k = 1
s = 1/2
sw = 0
while k<4:
    k = k + 1
    if sw == 0:
        s = s - (k/(k+1))
        sw = 1
    else:
        s = s + (k/(k+1))
        sw = 0
print(f'{s:.2f}')
    