#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (65.00%)
# Likes:    12176
# Dislikes: 404
# Total Accepted:    3.7M
# Total Submissions: 5.8M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1
        # O(nlogn + mlogm) -- 19%
        # simple, sort both, see if they are the same
        # return sorted(s) == sorted(t)

        # 2
        # O(n+m) -- 93.5%
        # use counter data structure to compare
        # from collections import Counter

        # return Counter(s) == Counter(t)

        # 3
        # O(n+m) -- 72%
        # implement counter solution by hand
        # count_s = {}
        # count_t = {}
        # for c in s:
        #     if c not in count_s:
        #         count_s[c] = 1
        #     else:
        #         count_s[c] += 1

        # for c in t:
        #     if c not in count_t:
        #         count_t[c] = 1
        #     else:
        #         count_t[c] += 1

        # return count_s == count_t

        # 4
        # O(n+m) -- 23%
        # use a single array to track
        # l = [0] * 26
        # for c in s:
        #     idx = ord(c) % 26
        #     l[idx] += 1
        # for c in t:
        #     idx = ord(c) % 26
        #     l[idx] -= 1
        #     if l[idx] < 0:
        #         return False
        # for v in l:
        #     if v != 0:
        #         return False
        # return True

        # 5
        # O(n+m) -- 63%
        # list index method without extra loop

        length = len(s)
        if length != len(t):
            return False

        l = [0] * 26
        for i in range(length):
            s_idx = ord(s[i]) % 26
            t_idx = ord(t[i]) % 26
            l[s_idx] += 1
            l[t_idx] -= 1

        for v in l:
            if v != 0:
                return False
        return True


# @lc code=end
