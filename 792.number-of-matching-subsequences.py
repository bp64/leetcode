#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (50.91%)
# Likes:    5499
# Dislikes: 234
# Total Accepted:    233.4K
# Total Submissions: 458.6K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
#
# Example 1:
#
#
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
#
#
# Example 2:
#
#
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # 1
        # O(s*words*words[i]) -- time limit exceeded
        # iterate through s
        # check if char in s matches first char of each subsequence
        # if so, remove first char from subsequence
        # and if subsequence is now empty, add to count
        # count = 0
        # for c in s:
        #     for i, word in enumerate(words):
        #         if word and word[0] == c:
        #             words[i] = word[1:]
        #             if not words[i]:
        #                 count += 1
        # return count

        # 2
        # O(words + s * words * words[i]) -- 52%
        # instead of iterating through words
        # use a dict[[str, list[str]]] to keep track of the next char
        # needed in the subsequence + the rest of the subsequence
        # then, as chars are found in the subsequence,
        # update the dict to reflect the next char needed
        d = {}
        for word in words:
            if word[0] not in d:
                d[word[0]] = [word[1:]]
            else:
                d[word[0]].append(word[1:])

        count = 0
        for c in s:
            if c not in d:
                continue

            temp = []
            for subseq in d[c]:
                if subseq == "":
                    count += 1
                    continue

                if subseq[0] == c:
                    temp.append(subseq[1:])
                else:
                    if subseq[0] not in d:
                        d[subseq[0]] = [subseq[1:]]
                    else:
                        d[subseq[0]].append(subseq[1:])

            d[c] = temp

        return count


# @lc code=end
