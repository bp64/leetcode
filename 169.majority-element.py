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
        # O(n) time, O(n) space -- 50%
        # count all elements in list, then return the greatest

        # d = {}
        # for n in nums:
        #     if n in d:
        #         d[n] += 1
        #     else:
        #         d[n] = 1
        # return max(d, key=d.get)

        # O(n) time, O(n) space -- 45%
        # iterate through and count
        # if the value is greater then half, return

        # if len(nums) == 1:
        #     return nums[0]
        # d = {}
        # target = len(nums) / 2
        # for n in nums:
        #     if n not in d:
        #         d[n] = 1
        #         continue

        #     d[n] += 1
        #     if d[n] > target:
        #         return n

        # return None  # no majority found

        # 3 Moores majority voting algorithm
        # O(n) time, O(1) space
        # ONLY WORKS WHEN FINDING MAJORITIES > N/2 + 1
        # keep a count of if a candidate number
        # is the same or not as the current number
        # if yes, increment, if no decrement
        # if the count drops to zero, use the current number as candidate and continue
        # since we are guaranteed at least an N/2 + 1 majority
        # we know the final candidate will be the true majority
        count = 0
        for n in nums:
            if count == 0:
                majority_candidate = n
                count += 1
                continue

            if n == majority_candidate:
                count += 1
            else:
                count -= 1

        return majority_candidate


# @lc code=end
