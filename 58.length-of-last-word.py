#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (52.86%)
# Likes:    5240
# Dislikes: 285
# Total Accepted:    2.1M
# Total Submissions: 4M
# Testcase Example:  '"Hello World"'
#
# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
# Example 1:
#
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
#
# Example 2:
#
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
#
# Example 3:
#
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
#
#
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1
        # O(n) -- 33%
        # iterate backwards, stop at first space after a seeing a word
        # count = 0
        # seen_word = False
        # for i in range(len(s), 0, -1):
        #     if s[i - 1] != " ":
        #         count += 1
        #         seen_word = True
        #     else:
        #         if seen_word:
        #             return count
        # return count

        # 2
        # rstrip -- 89%
        # strip trailing spaces to guarantee last char is part of word
        s = s.rstrip()
        count = 0
        for i in range(len(s), 0, -1):
            if s[i - 1] != " ":
                count += 1
            else:
                return count
        return count

        # 3
        # pythonic oneliner -- 76%
        # return len(s.rstrip().split(" ")[-1])


# @lc code=end
