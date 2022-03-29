"""
===== Initial Thoughts =====
use a stack
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        curr = head
        prev = None

        # go to beginning of where it needs to be reversed
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        
        # add reversed section to a stack
        stack = []
        for _ in range(left, right + 1):
            stack.append(curr)
            curr = curr.next
        
        # reattach
        while stack:
            node = stack.pop()
            if prev:
                prev.next = node
                prev = prev.next
            else:
                prev = node
                head = prev
        prev.next = curr
        return head
