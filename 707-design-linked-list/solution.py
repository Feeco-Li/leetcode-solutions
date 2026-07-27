# 707: Design Linked List
# Difficulty: Medium
# https://leetcode.com/problems/design-linked-list/
#
# Design your implementation of the linked list. You can choose to use a singly or
# doubly linked list.
# A node in a singly linked list should have two attributes: `val` and `next`.
# `val` is the value of the current node, and `next` is a pointer/reference to the
# next node.
# If you want to use the doubly linked list, you will need one more attribute
# `prev` to indicate the previous node in the linked list. Assume all nodes in the
# linked list are **0-indexed**.
#
# Implement the `MyLinkedList` class:
# * `MyLinkedList()` Initializes the `MyLinkedList` object.
# * `int get(int index)` Get the value of the `index^{th}` node in the linked
#   list. If the index is invalid, return `-1`.
# * `void addAtHead(int val)` Add a node of value `val` before the first element
#   of the linked list. After the insertion, the new node will be the first node
#   of the linked list.
# * `void addAtTail(int val)` Append a node of value `val` as the last element of
#   the linked list.
# * `void addAtIndex(int index, int val)` Add a node of value `val` before the
#   `index^{th}` node in the linked list. If `index` equals the length of the
#   linked list, the node will be appended to the end of the linked list. If
#   `index` is greater than the length, the node **will not be inserted**.
# * `void deleteAtIndex(int index)` Delete the `index^{th}` node in the linked
#   list, if the index is valid.
#
#
#
# **Example 1:**
#
# **Input**
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex",
#  "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# **Output**
# [null, null, null, null, 2, null, 3]
#
# **Explanation**
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#
#
#
# **Constraints:**
# * `0 <= index, val <= 1000`
# * Please do not use the built-in LinkedList library.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        # 1. 严格拦截越界索引 (合法范围: 0 <= index < self.size)
        if index < 0 or index >= self.size:
            return -1

        p: Optional[ListNode] = self.dummy_head.next

        # 2. 遍历 index 步
        for _ in range(index):
            if p is not None:
                p = p.next

        # 3. 类型窄化防护，消灭 Diagnostics 警告
        if p is None:
            return -1

        return p.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        # 从 dummy_head 开始走 index 步，精准停在【前驱节点】上
        prev = self.dummy_head
        for _ in range(index):
            if prev.next is not None:
                prev = prev.next

        # 插入新节点：新节点的 next 指向 prev.next，prev.next 再指向新节点
        prev.next = ListNode(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return

        # 从 dummy_head 开始走 index 步，精准停在【前驱节点】上
        prev = self.dummy_head
        for _ in range(index):
            if prev.next is not None:
                prev = prev.next

        # 插入新节点：新节点的 next 指向 prev.next，prev.next 再指向新节点
        if prev.next:
            prev.next = prev.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
