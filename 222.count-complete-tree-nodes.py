#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Easy (66.50%)
# Likes:    8694
# Dislikes: 523
# Total Accepted:    784.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = []
# Output: 0
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 1
        # O(n) -- 34%
        # naive, dfs
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1

        # return self.countNodes(root.left) + self.countNodes(root.right) + 1

        # 2
        # O(log^2(n))
        # binary search the leaf nodes to find the last leaf

        depth = self.calc_depth(root)

        # the number of nodes in a full binary tree
        # can be labeled with a bit string
        # with a depth 3 tree (2^3 nodes)
        # where the first node is 000, the last is 111

        # number of nodes in a complete tree is
        # (2^depth) - 1
        # nodes at level = 2^(depth-1)
        return

    def calc_depth(root: Optional[TreeNode]) -> int:
        depth = 0
        n = root
        while n:
            depth += 1
            n = n.left
        return depth


# @lc code=end
