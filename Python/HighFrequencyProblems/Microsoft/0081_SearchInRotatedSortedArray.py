"""
Search in rotated sorted array II
No duplicate value
"""

"""
one the top of my mind, we need to use the binary search
left = 0
right = len(nums)-1
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            mid = (left+right)//2
            if target == nums[mid]:
                return True
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False