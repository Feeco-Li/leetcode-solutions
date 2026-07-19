# 19: Remove Nth Node From End of List
# Difficulty: Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Given the `head` of a linked list, remove the `n^{th}` node from the end of the
# list and return its head.
#
#
#
# **Example 1:**
#
# **Input:** head = [1,2,3,4,5], n = 2
# **Output:** [1,2,3,5]
#
# **Example 2:**
#
# **Input:** head = [1], n = 1
# **Output:** []
#
# **Example 3:**
#
# **Input:** head = [1,2], n = 1
# **Output:** [1]
#
#
#
# **Constraints:**
# * The number of nodes in the list is `sz`.
# * `1 <= sz <= 30`
# * `0 <= Node.val <= 100`
# * `1 <= n <= sz`
#
#
#
# **Follow up:** Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the nth node from end
        p1 = head
        for i in range(n):
            p1 = p1.next
        p2 = head
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p = self.findFromEnd(dummy, n + 1)
        p.next = p.next.next
        return dummy.next
