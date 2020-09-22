inputStrList = list(input())
flag = True

for i in range(len(inputStrList)):
    newStrList = inputStrList[0:i] + inputStrList[i+1:len(inputStrList)]
    newStr = "".join(newStrList)
    if newStr == newStr[::-1]:
        flag = False
        print(newStr)
        break

if flag: print("false")

