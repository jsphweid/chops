"""
=== Brute Force Approach ===
put everything in a list first

~~Complexity Analysis
Time - O(n)
Space - O(n)

=== Implemented Approach ===
had to read "reverse second half" in discussions, but I think I get it

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find mid point
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        while fast:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next

        # disconnect
        slow.next = None

        # reverse second half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # find result
        l, r, res = head, prev, 0
        while l and r:
            res = max(res, l.val + r.val)
            l = l.next
            r = r.next
        return res


