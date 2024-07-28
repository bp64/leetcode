#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if nums2 == []:
            return

        j = 0
        k = 0

        out: list[int] = [0 for i in range(n + m)]

        for i in range(n + m):
            if j == m:
                out[i] = nums2[k]
                k += 1
                continue
            if k == n:
                out[i] = nums1[j]
                j += 1
                continue

            if nums1[j] < nums2[k]:
                v = nums1[j]
                j += 1
                out[i] = v

            else:
                v = nums2[k]
                k += 1
                out[i] = v

        for i in range(n + m):
            nums1[i] = out[i]


# @lc code=end
