#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (43.35%)
# Likes:    17637
# Dislikes: 4560
# Total Accepted:    3.5M
# Total Submissions: 8.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 1
        # O(n^2) - 96%
        # for each position in the prefix, check each char is the same

        if len(strs) == 0:
            return strs

        if len(strs) == 1:
            return strs[0]

        min_len = min([len(s) for s in strs])
        i = 0
        while i < min_len:
            prefix_char = strs[0][i]
            not_equal = False
            for s in strs[1:]:
                if s[i] != prefix_char:
                    not_equal = True
                    break
            if not_equal:
                break
            i += 1
        return strs[0][:i]


# @lc code=end
