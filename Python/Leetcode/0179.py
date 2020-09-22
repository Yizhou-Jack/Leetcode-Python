def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if str(nums[j])+str(nums[j+1]) < str(nums[j+1])+str(nums[j]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    res = ""
    for i in range(n):
        res += str(nums[i])
    return res

nums = [3,30,34,5,9]
print(largestNumber(nums))