"""
=== Brute Force Approach ===
one pass to get the length

~~Complexity Analysis
Time - O(n) - two-pass
Space - O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # get length
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next

        # position left pointer
        l, r = sorted([k - 1, N - k])
        left = right = dummy
        for _ in range(r):
            if l:
                left = left.next
                l -= 1
            right = right.next

        left.next.val, right.next.val = right.next.val, left.next.val

        return head
