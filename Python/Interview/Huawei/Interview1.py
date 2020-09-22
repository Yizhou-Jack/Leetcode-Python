def getHeight(n, times):
    return n/(2**(times-1))

def getTotalHeight(n, times):
    res = 0
    for i in range(times):
        if i == 0 or i == 1:
            res += n
            continue
        else:
            res += n/(2**(times-2))
    return res

n = 10
times = 5
print(getHeight(10, 5))
print(getTotalHeight(10, 5))
