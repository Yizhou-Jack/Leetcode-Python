n = int(input())
arr = list(map(int, input().split()))

maxArea = 0

stack = [0]
newArr = [-1] + arr + [-1]
for i in range(1, len(newArr)):
    while newArr[i] < newArr[stack[-1]]:
        curHeight = newArr[stack.pop()]
        curWidth = i - stack[-1] - 1
        maxArea = max(maxArea, curHeight * curWidth)
    stack.append(i)

print(maxArea)

