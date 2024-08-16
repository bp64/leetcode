#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (50.85%)
# Likes:    15572
# Dislikes: 1382
# Total Accepted:    3.2M
# Total Submissions: 6.2M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
# Constraints:
#
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#
#


# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1
        # O(n) -- 52%
        # iterate through list, track of seen ids
        # if head is None:
        #     return False

        # ids = set()

        # while head.next is not None:
        #     if id(head) in ids:
        #         return True
        #     ids.add(id(head))
        #     head = head.next

        # return False

        # 2
        # O(n) -- 14%
        # O(1) memory
        # two pointers, one iterating twice as fast as the other
        # if a cycle exists, the two pointers will overlap
        # if no cycle exists, the fast pointer finishes

        if head is None:
            return False

        fast_node = head
        if fast_node.next is None:
            return False
        fast_node = fast_node.next

        while True:
            if id(head) == id(fast_node):
                return True
            head = head.next

            if fast_node.next is None:
                return False
            fast_node = fast_node.next

            if fast_node.next is None:
                return False
            fast_node = fast_node.next


# @lc code=end
