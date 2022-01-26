#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  # type: ignore
        nums = []
        l    = len(nums1) + len(nums2)

        for _ in range(int(l/2)+1):
            if len(nums1):
                if len(nums2):
                    if nums1[0] > nums2[0]:
                        nums.append(nums2.pop(0))
                    else:
                        nums.append(nums1.pop(0))

                else:
                    nums += nums1
                    break

            elif len(nums2):
                nums += nums2
                break

        if l % 2 == 0:
            return (nums[int(l/2)-1] + nums[int(l/2)]) / 2
        else:
            return nums[int(l/2)]
# @lc code=end

