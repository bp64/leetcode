#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (64.88%)
# Likes:    21936
# Dislikes: 2140
# Total Accepted:    4.4M
# Total Submissions: 6.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
#
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 1
        # O(n + m) -- 81%
        # compare the two smallest nodes in each list
        # set aside the smallest node, increment it's owner to the next node
        # set the smallest node to be the next node in the merged list
        # repeat
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # choose node for merged list and next that list
        if list1.val < list2.val:
            merged_list = list1
            list1 = list1.next
        else:
            merged_list = list2
            list2 = list2.next

        # note the head node of the merged list
        merged_head = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            merged_list = merged_list.next

        nonempty_node = list1 if list1 else list2
        merged_list.next = nonempty_node

        return merged_head


# @lc code=end
