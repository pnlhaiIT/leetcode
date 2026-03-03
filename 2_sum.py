class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] == target:
                result.append(i)
                result.append(i+1)
                return result

nums = [3,2,4]
target = 6
kq = Solution().twoSum(nums,target)
print(kq)
