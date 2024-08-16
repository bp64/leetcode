#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.81%)
# Likes:    24180
# Dislikes: 1782
# Total Accepted:    4.9M
# Total Submissions: 12M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 1
        # O(n) -- 87%
        # use a list as a stack
        d = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
                continue

            if stack == []:
                return False

            v = stack.pop()
            if c != d[v]:
                return False

        if stack != []:
            return False

        return True


# @lc code=end
