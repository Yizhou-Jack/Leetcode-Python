"""
Check bit in in position i (right to left) is 1 or not
"""
def checkBit(n, i):
    return (n & (1 << i)) != 0