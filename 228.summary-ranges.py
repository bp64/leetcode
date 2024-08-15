#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Easy (51.18%)
# Likes:    3969
# Dislikes: 2174
# Total Accepted:    606.4K
# Total Submissions: 1.2M
# Testcase Example:  '[0,1,2,4,5,7]'
#
# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. That is, each element of nums is covered by exactly one of the
# ranges, and there is no integer x such that x is in one of the ranges but not
# in nums.
#
# Each range [a,b] in the list should be output as:
#
#
# "a->b" if a != b
# "a" if a == b
#
#
#
# Example 1:
#
#
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
#
# Example 2:
#
#
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
#
#
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # 1
        # O(n) -- 84%
        # iterate through and add to range as needed
        # asdflakjsdflas soooo difficult for me
        if len(nums) == 0:
            return []

        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(str(nums[i]))
                continue

            if nums[i] == nums[i - 1] + 1:
                continue

            # end the previous range, if it needs
            if out[-1] != str(nums[i - 1]):
                out[-1] += "->" + str(nums[i - 1])

            # start the next range
            out.append(str(nums[i]))

        # if the last element was part of a previous sequence add it back
        if nums[i] == nums[i - 1] + 1:
            out[-1] += "->" + str(nums[i])

        return out


# @lc code=end
