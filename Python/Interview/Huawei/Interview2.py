def getOneNumber(inputList):
	res = inputList[0]
	for i in range(1, len(inputList)):
		res = res^inputList[i]
	return res

print(getOneNumber([1,2,3,4,1,3,4]))
