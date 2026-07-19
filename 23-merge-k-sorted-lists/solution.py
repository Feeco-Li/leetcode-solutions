# 23: Merge k Sorted Lists
# Difficulty: Hard
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# You are given an array of `k` linked-lists `lists`, each linked-list is sorted
# in ascending order.
#
# *Merge all the linked-lists into one sorted linked-list and return it.*
#
#
#
# **Example 1:**
#
# **Input:** lists = [[1,4,5],[1,3,4],[2,6]]
# **Output:** [1,1,2,3,4,4,5,6]
# **Explanation:** The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
#
# **Example 2:**
#
# **Input:** lists = []
# **Output:** []
#
# **Example 3:**
#
# **Input:** lists = [[]]
# **Output:** []
#
#
#
# **Constraints:**
# * `k == lists.length`
# * `0 <= k <= 10⁴`
# * `0 <= lists[i].length <= 500`
# * `-10⁴ <= lists[i][j] <= 10⁴`
# * `lists[i]` is sorted in **ascending order**.
# * The sum of `lists[i].length` will not exceed `10⁴`.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(-1)
        d = dummy
        pq = []

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(pq, (node.val, i, node))

        while pq:
            val, i, node = heapq.heappop(pq)
            d.next = node
            d = d.next
            print(val)

            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))

        return dummy.next
