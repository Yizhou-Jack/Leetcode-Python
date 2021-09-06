"""
Time: O(NlogN)
Space: O(N)
"""
class Solution1:
    def findNoKSortedArrays(self, nums1, nums2):
        k = (len(nums1)+len(nums2)+1)//2
        nums = nums1 + nums2
        nums.sort()
        return nums[k]

"""
Time: O(N)
Space: O(1)
"""
class Solution2:
    def findNoKSortedArrays(self, nums1, nums2):
        k = (len(nums1)+len(nums2)+1)//2
        if len(nums1) == 0: return nums2[k]
        elif len(nums2) == 0: return nums1[k]

        i = -1
        j = -1
        number = float('inf')
        while i < len(nums1) or j < len(nums2):
            if i+j+2 == k:
                break
            if i == len(nums1)-1 or (j+1 != len(nums2) and nums1[i+1] > nums2[j+1]):
                j += 1
                number = nums2[j]
            elif j == len(nums2)-1 or (i+1 != len(nums1) and nums1[i+1] <= nums2[j+1]):
                i += 1
                number = nums1[i]
        return number

"""
Time: O(logN)
Space: O(1)
"""
class Solution3:
    def findNoKSortedArrays(self, nums1, nums2):
        k = (len(nums1)+len(nums2)+1)//2

        index1 = 0
        index2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while True:
            if index1 == len1:
                return nums2[index2+k-1]
            if index2 == len2:
                return nums1[index1+k-1]
            if k == 1:
                return min(nums1[index1], nums2[index2])
            newIndex1 = min(index1 + k//2-1, len1-1)
            newIndex2 = min(index2 + k//2-1, len2-1)
            if nums1[newIndex1] > nums2[newIndex2]:
                k -= newIndex2-index2+1
                index2 = newIndex2+1
            else:
                k -= newIndex1-index1+1
                index1 = newIndex1+1

solution = Solution2()
res = solution.findNoKSortedArrays([1,3,5], [2,4])
print(res)