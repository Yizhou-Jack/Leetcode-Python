"""
Follow up: Find contiguous sub-array of which contains all the chars in the array
"""

"""
Time: O(N)
"""
def solution(nums):
    elementDict = {}
    left = 0
    right = 0
    res = float('inf')
    while right < len(nums):
        value = elementDict.get(nums[right], 0)
        if value == 0:
            res = right-left+1
        value += 1
        elementDict[nums[right]] = value
        while elementDict[nums[left]] > 1:
            elementDict[nums[left]] -= 1
            left += 1
            res = min(res, right-left+1)
        right += 1
    if res == float('inf'): return len(nums)
    return res

nums = list("fabcdbakbcfbcdeajahabcdefhj")
res = solution(nums)
print(res)

