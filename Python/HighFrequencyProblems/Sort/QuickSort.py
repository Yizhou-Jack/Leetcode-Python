def quickSort1(nums):
    if not nums or len(nums) == 1:
        return nums
    base = nums[0]
    leftList, rightList = [], []
    for i in nums[1:]:
        if i >= base:
            rightList.append(i)
        else:
            leftList.append(i)
    leftList = quickSort1(leftList)
    rightList = quickSort1(rightList)
    return leftList + [base] + rightList

def quickSort2(nums, start, end):
    if start >= end:
        return
    left = start
    right = end
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    quickSort2(nums, start, left-1)
    quickSort2(nums, left+1, end)

nums = [5,1,4,8,2,7,6]
quickSort2(nums,0,len(nums)-1)
print(nums)