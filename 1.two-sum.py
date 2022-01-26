#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # type: ignore
        neg = False
        for n in nums:
            if n < 0:
                neg = True
                break

        for i in range(len(nums)):
            if (not neg) and (nums[i] > target):
                continue
 
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
# @lc code=end

