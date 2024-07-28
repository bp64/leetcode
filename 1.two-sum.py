#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # 1 O(n^2)
        # for each number, check every other number

        # 2 O(nlogn)
        # sort list
        # iterate through list once

        # 3 O(n)
        # add to hash map and check if number exists
        seen = {}
        for i, v in enumerate(nums):
            s = target - v
            if s in seen:
                return [i, seen[s]]
            seen[v] = i


# @lc code=end
