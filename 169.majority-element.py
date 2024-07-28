#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (65.06%)
# Likes:    19236
# Dislikes: 634
# Total Accepted:    3.1M
# Total Submissions: 4.8M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # O(n)
        # count all elements in list, then return the greatest

        # d = {}
        # for n in nums:
        #     if n in d:
        #         d[n] += 1
        #     else:
        #         d[n] = 1
        # return max(d.items(), key=lambda x: x[1])[0]

        # O(n)
        # iterate through and count
        # if value is greater then half, return
        if len(nums) == 1:
            return nums[0]

        d = {}
        target = len(nums) / 2
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                if d[n] > target:
                    return n

        return None  # no majority found


# @lc code=end
