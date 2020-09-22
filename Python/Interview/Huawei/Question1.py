import sys

def solution(nums):
    numsLists = []
    for num in nums:
        numsLists.append(list(str(bin(num)[2:])))
    numsLists2 = []
    #change
    for numList in numsLists:
        length = len(numList)
        addList = []
        for i in range(32-length):
            addList.append("0")
        newNumsList = addList + numList
        for i in range(0,32,2):
            tmp = newNumsList[i]
            newNumsList[i] = newNumsList[i+1]
            newNumsList[i+1] = tmp
        numsLists2.append("".join(newNumsList))
    #move
    length = len(numsLists2)
    move1 = numsLists2[length-1][30:32]
    move2 = numsLists2[0][0:30]
    outputList = []
    outputList.append(str(int(move1+move2,2)))
    if length == 1:
        print("".join(outputList))
    else:
        for i in range(length-1):
            move1 = numsLists2[i][30:32]
            move2 = numsLists2[i+1][0:30]
            subRes = str(int(move1+move2, 2))
            outputList.append(subRes)
        print(" ".join(outputList))


if __name__ == "__main__":
    #print(int('11000000000000000000000000000010',2))
    #print(bin(2))
    #print(int('0100',2))
    nums = sys.stdin.readline().strip()
    nums = nums.split(" ")
    numsList = []
    for i in nums:
        numsList.append(int(i))
    solution(numsList)
