#计算数位之和
def sums(x):
    s = 0
    while x != 0:
        s += x % 10
        x = x // 10
    return s
print(sums(1234))