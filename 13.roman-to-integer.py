#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (62.04%)
# Likes:    14297
# Dislikes: 946
# Total Accepted:    3.9M
# Total Submissions: 6.2M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
#
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
#
# Example 2:
#
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 3:
#
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
#
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # 1
        # O(n) -- 90%
        # check element and element ahead and determine what number to add
        # val = 0
        # i = 0
        # while i < len(s):
        #     if i == len(s) - 1:
        #         val += lookup[s[i]]
        #         i += 1
        #         continue

        #     cur_val = lookup[s[i]]
        #     next_val = lookup[s[i + 1]]

        #     if cur_val < next_val:
        #         val += next_val - cur_val
        #         i += 2
        #     else:
        #         val += cur_val
        #         i += 1
        # return val

        # 2
        # O(n) -- 90%
        # check the element ahead to determine whether to add or subtract the current element
        val = 0
        for i in range(len(s) - 1):
            cur_val = lookup[s[i]]
            next_val = lookup[s[i + 1]]

            if next_val <= cur_val:
                val += cur_val
            else:
                val -= cur_val

        val += lookup[s[-1]]

        return val


# @lc code=end
