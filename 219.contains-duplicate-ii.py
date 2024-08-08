#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (45.93%)
# Likes:    6169
# Dislikes: 3098
# Total Accepted:    1M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # 1
        # O(n^2)
        # iterate through the array
        # only checking k distance apart or less elements for matches
        # if len(nums) < 2:
        #     return False
        # if k < 1:
        #     return False

        # i = 0
        # j = 1
        # while i < len(nums) - 1:
        #     if nums[i] == nums[j]:
        #         return True

        #     j += 1
        #     if (j - i > k) or (j == len(nums)):
        #         i += 1
        #         j = i + 1

        # return False

        # 2
        # O(nlogn) -- 5%
        # sort arrays and idx of arrays then compare the similar numbers

        if len(nums) < 2:
            return False
        if k < 1:
            return False

        from operator import itemgetter

        sorted_nums = sorted(zip(nums, range(len(nums))), key=itemgetter(0, 1))

        prev_n = None
        prev_idx = None
        for i in range(len(sorted_nums)):
            n, idx = sorted_nums[i]
            if prev_n != n:
                prev_n = n
                prev_idx = idx
            else:
                if idx - prev_idx <= k:
                    return True
                prev_idx = idx
        return False


# @lc code=end
