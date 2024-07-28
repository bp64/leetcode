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

        nums_w_idxs = sorted([(i, v) for i, v in enumerate(nums)], key=lambda x: x[1])

        i = 0
        j = len(nums) - 1
        target_not_found = True
        while target_not_found:
            s = target - nums_w_idxs[i][1]
            f = nums_w_idxs[j][1]

            if s == f:
                return (nums_w_idxs[i][0], nums_w_idxs[j][0])
            elif s > f:
                i += 1
            elif s < f:
                j -= 1


# @lc code=end
