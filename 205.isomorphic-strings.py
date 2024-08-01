#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (45.48%)
# Likes:    9036
# Dislikes: 2098
# Total Accepted:    1.4M
# Total Submissions: 3.1M
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
#
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
#
#
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 1
        # O(n) -- 5%
        # iterate through one string, track the mapping to other
        # if the mapping is ever wrong return false
        # if len(s) != len(t):
        #     return False

        # lookup = {}
        # reverse_lookup = {}
        # for i in range(len(s)):
        #     match s[i] in lookup, t[i] in reverse_lookup:
        #         case False, False:
        #             lookup[s[i]] = t[i]
        #             reverse_lookup[t[i]] = s[i]
        #         case True, True:
        #             if (lookup[s[i]] != t[i]) or (reverse_lookup[t[i]] != s[i]):
        #                 return False
        #         case _:
        #             return False

        # return True

        # 2
        # O(n) -- 5%
        # iterate through one string, track the mapping to other

        # 1
        # O(n^2) -- 80%, pythonic
        # iterate through one string, track the mapping to other
        # if the mapping is ever wrong return false
        if len(s) != len(t):
            return False

        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                if t[i] in lookup.values():
                    return False
                lookup[s[i]] = t[i]
                continue

            if lookup[s[i]] != t[i]:
                return False

        return True


# @lc code=end
