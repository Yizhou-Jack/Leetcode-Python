"""
Time: O(NlogN)
Space: O(N)
"""
class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+len2) % 2 == 1:
            k = (len1+len2+1)//2
            nums = nums1 + nums2
            nums.sort()
            return nums[k]
        else:
            k1 = (len1+len2+1)//2
            k2 = k1+1
            nums = nums1 + nums2
            nums.sort()
            return (nums[k1]+nums2[k2])/2

"""
Time: O(N)
Space: O(1)
"""
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 + len2 == 1: return nums1[0] if len1 == 1 else nums2[0]

        k = (len1+len2+1)//2
        if len1 == 0: return nums2[k]
        elif len2 == 0: return nums1[k]

        i = -1
        j = -1
        number1 = float('inf')
        while i < len1 or j < len2:
            if i+j+2 == k:
                break
            if i == len1-1 or (j+1 != len2 and nums1[i+1] > nums2[j+1]):
                j += 1
                number1 = nums2[j]
            elif j == len2-1 or (i+1 != len1 and nums1[i+1] <= nums2[j+1]):
                i += 1
                number1 = nums1[i]

        if (len1+len2) % 2 == 1:
            return number1
        else:
            if i == len1-1:
                number2 = nums2[j+1]
            elif j == len2-1:
                number2 = nums1[i+1]
            else:
                number2 = nums1[i+1] if nums1[i+1] < nums2[j+1] else nums2[j+1]
            return (number1+number2)/2


"""
Time: O(logN)
Space: O(1)
"""
class Solution3:
    def findMedianSortedArrays(self, nums1, nums2):
        k = (len(nums1)+len(nums2)+1)//2

        len1 = len(nums1)
        len2 = len(nums2)
        def getNoK(k):
            index1 = 0
            index2 = 0
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

        if (len1+len2) % 2 == 1:
            return getNoK(k)
        else:
            return (getNoK(k)+getNoK(k+1))/2

solution = Solution3()
res = solution.findMedianSortedArrays([1,3], [2,4])
print(res)