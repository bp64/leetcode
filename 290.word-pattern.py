#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.25%)
# Likes:    7261
# Dislikes: 1029
# Total Accepted:    759K
# Total Submissions: 1.8M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 1
        # O(n) -- 19%
        # similar to isomorphic-strings
        # split s by white space
        # iterate through pattern, track mappings from chars to words and words to chars
        # if word or char isn't in lookup, insert the map, ie. write once
        # then check what is in the lookup conforms with the current word
        # and vice versa

        # words = s.split()
        # if len(pattern) != len(words):
        #     return False

        # lookup = {}
        # rlookup = {}
        # for i, c in enumerate(pattern):
        #     if c not in lookup:
        #         lookup[c] = words[i]
        #     if words[i] not in rlookup:
        #         rlookup[words[i]] = c
        #     if (lookup[c] != words[i]) or (rlookup[words[i]] != c):
        #         return False
        # return True

        # 2
        # O(n) -- 84%
        # use set properties

        words = s.split()

        # check there is a word for each char in pattern
        if len(pattern) != len(words):
            return False

        # check the number unique chars equals the number of unique words
        # then check that equals the number of unique mappings
        # ie. no character is mapped to two different words and vice-versa
        mappings = set(zip(pattern, words))
        return len(set(pattern)) == len(set(words)) == len(mappings)


# @lc code=end
