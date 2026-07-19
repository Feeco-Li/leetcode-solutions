# 328: Odd Even Linked List
# Difficulty: Medium
# https://leetcode.com/problems/odd-even-linked-list/
#
# Given the `head` of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return *the reordered
# list*.
#
# The **first** node is considered **odd**, and the **second** node is **even**,
# and so on.
#
# Note that the relative order inside both the even and odd groups should remain
# as it was in the input.
#
# You must solve the problem in `O(1)` extra space complexity and `O(n)` time
# complexity.
#
#
#
# **Example 1:**
#
# **Input:** head = [1,2,3,4,5]
# **Output:** [1,3,5,2,4]
#
# **Example 2:**
#
# **Input:** head = [2,1,3,5,6,4,7]
# **Output:** [2,3,6,7,1,5,4]
#
#
#
# **Constraints:**
# * The number of nodes in the linked list is in the range `[0, 10⁴]`.
# * `-10⁶ <= Node.val <= 10⁶`

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(-1), ListNode(-1)
        pOdd, pEven = odd, even
        p = head
        counter = 1

        while p:
            if counter % 2 != 0:
                pOdd.next = p
                pOdd = pOdd.next
            else:
                pEven.next = p
                pEven = pEven.next
            p = p.next
            counter += 1
        pEven.next = None
        pOdd.next = even.next
        return odd.next
