import sys

def solution(width, height):
    n = len(width)
    stack = []
    stack.append((-1, -1))
    maxs = 0
    cur = 0
    for i in range(n):
        tmp = stack[-1]
        if tmp[0] >= height[i]:
            site = tmp[1]
            while tmp[0] > height[i]:
                cur = tmp[0]*sum(width[tmp[1]:i])
                maxs = max(cur, maxs)
                site = tmp[1]
                stack.pop()
                tmp = stack[-1]
            p = (height[i], site)
        else:
            p = (height[i], i)
        stack.append(p)
    while len(stack) != 0:
        tmp = stack[-1]
        if tmp[0] != -1:
            cur = tmp[0]*sum(width[tmp[1]:n-1])
            maxs = max(cur, maxs)
        stack.pop()
    return maxs


if __name__ == "__main__":
    line = input()
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.split(',')

    inputArray = []
    width = []
    length = []
    flag = True

    for i in range(len(line)):
        if 0 <= int(line[i]) <= 100:
            inputArray.append(int(line[i]))
        else:
            flag = False
            break
    if flag:
        length = len(inputArray)
        length = int(length/2)
        width = inputArray[0:length]
        height = inputArray[length:]
        print(solution(width, height))
    else:
        print(0)