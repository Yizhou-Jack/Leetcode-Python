nmr = input().split(" ")
n = float(nmr[0])
m = int(nmr[1])
r = float(nmr[2])

oneRound = 4*n
for i in range(1, m+1):
    length = (r*i) % oneRound
    if 0 <= length < n:
        strX = '%.2f' % length
        strY = '0.00'
    elif n <= length < 2*n:
        strX = '%.2f' % n
        strY = '%.2f' % (length-n)
    elif 2*n <= length < 3*n:
        strX = '%.2f' % (3*n-length)
        strY = '%.2f' % n
    else:
        strX = '0.00'
        strY = '%.2f' % (4*n-length)
    print(strX + ' ' + strY)