#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (62.13%)
# Likes:    4998
# Dislikes: 501
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1
        # O(nm) - 72%
        # pythonic, iterate through note, remove from magazine, if exists
        for c in ransomNote:
            idx = magazine.find(c)
            if idx == -1:
                return False
            if idx == len(magazine) - 1:
                magazine = magazine[:idx]
            else:
                magazine = magazine[:idx] + magazine[idx + 1 :]
        return True


# @lc code=end
