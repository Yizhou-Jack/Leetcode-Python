str = input()
strList = list(str)
length = len(strList)

resList = []
i = 0
flag = False
while i < length:
    if (not strList[i].isdigit()) and (not strList[i].isalpha()):
        i += 1
        flag = True
        continue
    elif strList[i].isdigit():
        resList.append(strList[i])
        i += 1
        flag = False
    else:
        if len(resList) == 0:
            resList.append(strList[i].lower())
            i += 1
            flag = False
            continue
        if flag:
            resList.append(strList[i].upper())
            i += 1
            flag = False
        else:
            resList.append(strList[i].lower())
            i += 1
            flag = False
print("".join(resList))