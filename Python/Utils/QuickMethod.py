import math

# Calculate the sum of digit
def sums(x):
    s = 0
    while x != 0:
        s += x % 10
        x = x // 10
    return s
print(sums(1234))

# Calculate the prime number that can divide by n
def primeSet(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return primeSet(n//i) | {i}
    return {n}