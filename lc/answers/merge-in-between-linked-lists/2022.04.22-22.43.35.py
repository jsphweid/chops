"""
seems pretty straight-forward, just gotta be careful
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = list1
        left = list1
        for _ in range(a - 1):
            left = left.next
        right = left
        for _ in range(b - a + 2):
            right = right.next
        left.next = list2
        end = list2
        while end.next:
            end = end.next
        end.next = right
        return res
