"""
变形：给定一个正整数 n，找出大于 n 的非负整数中，其二进制表示不包含连续的1的最小值
"""

"""
Time: O(2^n)
Space: O(1)
"""
def solution1(n):
    number = n
    while True:
        number += 1
        bitList = list(bin(number)[2:])
        flag = True
        for i in range(1, len(bitList)):
            if bitList[i-1] == bitList[i] == '1':
                flag = False
                break
        if flag:
            return number

"""
Time: O(N)
"""
def solution2(n):
    bitN = bin(n)[2:]
    index00 = bitN.rfind('00')
    if index00 == -1:
        return int('1' + '0'*len(bitN), 2)
    else:
        index11 = bitN.find('11')
        if index11 == -1: #No 11 but have 00 => have 01 => change 00 to 01 and add 0 after it
            return int(bitN[0:index00+1] + '1' + '0'*len(bitN[index00+2:]), 2)
        else:
            newIndex00 = bitN[0:index11].rfind('00')
            if newIndex00 == -1:
                return int('1' + '0'*len(bitN), 2)
            else:
                return int(bitN[0:newIndex00+1] + '1' + '0'*len(bitN[newIndex00+2:]), 2)

n = 5447
k = solution1(n)
m = solution2(n)
print(k)
print(m)
for i in range(10,100000):
    n = i
    m = solution1(n)
    k = solution2(n)
    if m != k:
        print(n)
