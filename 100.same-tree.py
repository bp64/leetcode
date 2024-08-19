#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (62.86%)
# Likes:    11604
# Dislikes: 242
# Total Accepted:    2.3M
# Total Submissions: 3.7M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
#
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1
        # O(n + m) -- 43%
        # break each tree into a subtree and recurse
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        is_left_same = self.isSameTree(p.left, q.left)
        is_right_same = self.isSameTree(p.right, q.right)
        return is_left_same and is_right_same


# @lc code=end
