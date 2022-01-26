#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        substr  = ''
        longest = 0

        for i in range(len(s)):
            if len(s) - i <= longest:
                break

            for j in range(i, len(s)):
                if s[j] not in substr:
                    substr += s[j]

                else:
                    if len(substr) > longest:
                        longest = len(substr)

                    substr = ''
                    break

        if len(substr) > longest:
            longest = len(substr)

        return longest
# @lc code=end

