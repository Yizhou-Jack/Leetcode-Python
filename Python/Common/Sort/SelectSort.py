def selectSort(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[minIndex] > nums[j]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]

nums = [5,1,4,8,2,7,6]
selectSort(nums)
print(nums)