class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        median = 0

        if len(nums)%2 == 0:
            mid = len(nums)//2
            median = (nums[mid-1] + nums[mid]) / 2 
        else:
            mid = len(nums)//2
            median = nums[mid]

        return median     

'''
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
nums1 = [1,2] 
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1,nums2))