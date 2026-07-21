# 21: Merge Two Sorted Lists
# Difficulty: Easy
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# You are given the heads of two sorted linked lists `list1` and `list2`.
#
# Merge the two lists into one **sorted** list. The list should be made by
# splicing together the nodes of the first two lists.
#
# Return *the head of the merged linked list*.
#
#
#
# **Example 1:**
#
# **Input:** list1 = [1,2,4], list2 = [1,3,4]
# **Output:** [1,1,2,3,4,4]
#
# **Example 2:**
#
# **Input:** list1 = [], list2 = []
# **Output:** []
#
# **Example 3:**
#
# **Input:** list1 = [], list2 = [0]
# **Output:** [0]
#
#
#
# **Constraints:**
# * The number of nodes in both lists is in the range `[0, 50]`.
# * `-100 <= Node.val <= 100`
# * Both `list1` and `list2` are sorted in **non-decreasing** order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        if l1 is None:
            p.next = l2
        else:
            p.next = l1
        return dummy.next
