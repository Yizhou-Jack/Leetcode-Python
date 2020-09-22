class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[right] < nums[mid]:
                left = mid+1
            else:
                right = mid
        return nums[left]

solution = Solution()
res = solution.findMin([4,5,6,7,0,1,2])
print(res)