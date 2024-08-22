#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (73.01%)
# Likes:    5282
# Dislikes: 327
# Total Accepted:    544.4K
# Total Submissions: 744.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10^-5 of the actual answer
# will be accepted.
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
#
# Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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


from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        # 1
        # O(n) -- 96%
        # use bfs with a queue and track avgs with a list
        # deques are O(1) to pop(0), where lists are O(n)
        # queue: deque[TreeNode] = deque()
        # avgs: list[float] = []

        # root.depth = 0
        # queue.append(root)

        # count = 0
        # sum = 0
        # while queue:
        #     n = queue.popleft()

        #     if n.left:
        #         n.left.depth = n.depth + 1
        #         queue.append(n.left)
        #     if n.right:
        #         n.right.depth = n.depth + 1
        #         queue.append(n.right)

        #     count += 1
        #     sum += n.val

        #     if not queue or queue[0].depth != n.depth:
        #         avgs.append(sum / count)
        #         count = 0
        #         sum = 0

        # return avgs

        # 2
        # O(n) -- 68%
        # bfs, add each level to queue then process all nodes, repeat
        # O(logn) memory
        queue: deque[TreeNode] = deque()
        avgs: list[float] = []

        queue.append(root)

        while queue:
            lenq = len(queue)
            count = 0
            total = 0
            for _ in range(lenq):
                n = queue.popleft()

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

                count += 1
                total += n.val

            avgs.append(total / count)

        return avgs


# @lc code=end
