#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(x)[1:][::-1])

        if x < -2147483648 or x > 2147483647:
            return 0
        else:
            return x
# @lc code=end

