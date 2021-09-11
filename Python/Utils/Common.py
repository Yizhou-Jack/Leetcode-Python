# 将字符串转为大写
testStr = "abc"
res = testStr.upper()
print(res)

# 将字符串转为大写
testStr = "ABC"
res = testStr.lower()
print(res)

# 找字符串中某字符第一次出现的位置（找不到返回-1）
testStr = "ABCA"
res = testStr.find('A')
print(res)

# 找字符串中某字符最后一次出现的位置（找不到返回-1）
testStr = "ABCA"
res = testStr.rfind('A')
print(res)

# 判断String是否只由数字组成
testString = "15"
res = testString.isdigit()
print(res)

# 判断String是否只由字母组成
testString = "ab"
res = testString.isalpha()
print(res)

# 字符串反转
testString = "huowuzhao"
res = testString[::-1]
print(res)

# 数字符串里出现了几次某字符
testString = '00100'
res = testString.count('00')
print(res)

# 十进制转二进制
testInt = 10
trans = bin(testInt)
print(trans) # 0b1010

# String list转为Int list
testList = ['1', '4', '3', '6', '7']
testList = [int(i) for i in testList]
print(testList)

# Int list转为String
testList = [1, 4, 3, 6, 7]
testString = "".join([str(i) for i in testList])
print(testString)

# char to number
resNumber = ord('a')
print(resNumber) # 97

# number to char
resChar = chr(97)
print(resChar) # 'a'