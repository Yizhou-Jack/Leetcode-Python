"""
给定一些数字属于1到9，给一个上限数字upper.
比如upper为990， 给定的数字为7,8,9， 那么不超过这个上限数字且只包含给定数字的最大数为989
upper为1000，给定的数字为1,2,3， 那么不超过这个上限数字且只包含给定数字的最大数为333
"""

def findMax(upper, nums):
    nums.sort()
    site = [-1 for _ in range(10)]
    for i in range(len(nums)):
        site[nums[i]] = i

    para = -1
    for i in range(10):
        if site[i] != -1:
            para = site[i]
        else:
            site[i] = para

    numsOfUpper = list(map(int, list(str(upper))))
    preFlag = True
    for i in range(len(numsOfUpper)):
        if numsOfUpper[i] not in nums:
            preFlag = False
    if preFlag: return upper

    length = len(numsOfUpper)
    res = []

    flag = -1
    for i in range(length):
        if numsOfUpper[i] in nums:
            res.append(str(numsOfUpper[i]))
            if site[numsOfUpper[i]] != 0:
                flag = i
        else:
            if site[numsOfUpper[i]] > -1:
                flag = i
            break

    if flag == -1:
        res = ["0"]
    else:
        res = res[:flag]
        if numsOfUpper[flag] in nums:
            res.append(str(nums[site[numsOfUpper[flag]]-1]))
        else:
            res.append(str(nums[site[numsOfUpper[flag]]]))

    while len(res) != length:
        res.append(str(nums[-1]))

    if res[0] == "0":
        return "".join(res[1:])
    return "".join(res)


res = findMax(3333330, [6, 3, 9])
print(res)