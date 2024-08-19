#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (57.14%)
# Likes:    15347
# Dislikes: 384
# Total Accepted:    2.1M
# Total Submissions: 3.7M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
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
    # 1
    # O(n) -- 75%
    # recurse through tree, checking if each node is symmetric
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root.left, root.right)

    def sym(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False

        return (
            r1.val == r2.val
            and self.sym(r1.left, r2.right)
            and self.sym(r1.right, r2.left)
        )


# @lc code=end
