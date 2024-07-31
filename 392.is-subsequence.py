#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (48.09%)
# Likes:    9634
# Dislikes: 534
# Total Accepted:    1.5M
# Total Submissions: 3.2M
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
# >= 10^9, and you want to check one by one to see if t has its subsequence. In
# this scenario, how would you change your code?
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # this is tricky because I forgot that when
        # s = "abc" t = "azzzzzabc"
        #                ^     ^
        # we don't need to match the second "a",
        # I tried to solve this problem with the extra constraint
        # "there can be no characters in the subsequence repeated"
        # s = "abc" t = "abzzzzac"
        # there would be no match here because the second a would 'reset' the sequence
        # so silly

        # 1
        # O(n) -- 21%
        # iterate through and compare with subseq

        # if len(s) == 0:
        #     return True
        # if len(t) == 0:
        #     return False

        # idx_in_s = 0
        # for c in t:
        #     if c != s[idx_in_s]:
        #         continue
        #     idx_in_s += 1
        #     if idx_in_s == len(s):
        #         return True
        # return False

        # 2
        # O(n) -- 79%
        # pythonic
        for i, c in enumerate(s):
            idx = t.find(c)
            # false if next character isn't found
            if idx == -1:
                return False

            # false if next character is found, but
            # but to near the end of the str that the
            # rest of the subsequence can't fit
            if idx + len(s) - i > len(t):
                return False
            t = t[idx + 1 :]

        return True


# @lc code=end
