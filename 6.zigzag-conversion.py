#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        for i in range(numRows):
            rows.append('')

        r = 0
        c = 1
        for i in range(len(s)):
            rows[r] += s[i]

            if numRows > 1:
                r += c
                if r == numRows-1:
                    c = -1
                elif r == 0:
                    c = 1

        ret = ''
        for r in rows:
            ret += r

        return ret
# @lc code=end

