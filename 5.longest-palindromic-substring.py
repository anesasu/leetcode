#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            if len(longest) >= (len(s) - i):
                break

            offset = len(longest)
            for j in range(i+offset, len(s)):
                if s[i] != s[j]:
                    continue

                ss = s[i:j+1]
                if ss == ss[::-1]:
                    longest = ss

        return longest
# @lc code=end

