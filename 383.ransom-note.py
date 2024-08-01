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
        # for c in ransomNote:
        #     idx = magazine.find(c)
        #     if idx == -1:
        #         return False
        #     if idx == len(magazine) - 1:
        #         magazine = magazine[:idx]
        #     else:
        #         magazine = magazine[:idx] + magazine[idx + 1 :]
        # return True

        # 2
        # O(n+m) -- 16%
        # convert both to dicts {char: count}, subtract
        # note = {}
        # for c in ransomNote:
        #     if c not in note:
        #         note[c] = 1
        #     else:
        #         note[c] += 1

        # mag = {}
        # for c in magazine:
        #     if c not in mag:
        #         mag[c] = 1
        #     else:
        #         mag[c] += 1

        # for c in note:
        #     if (c not in mag) or (mag[c] - note[c] < 0):
        #         return False
        # return True

        # 3
        # O(n+m) -- 66%
        # counters
        from collections import Counter

        # count each
        note = Counter(ransomNote)
        mag = Counter(magazine)

        # find the intersection of the counters
        # ie. min(note[c], mag[c])
        # if the result == note, then there are enough
        # elements to satisfy creating the note
        return note & mag == note


# @lc code=end
