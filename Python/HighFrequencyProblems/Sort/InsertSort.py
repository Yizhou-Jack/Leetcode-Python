def insertSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
            nums[j + 1] = key

nums = [12, 11, 13, 5, 6]
insertSort(nums)
print(nums)