"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        anchor = ListNode(0)
        anchor.next = head
        while head.next:
            nxt = head.next
            anchor.next, head.next, nxt.next = nxt, nxt.next, anchor.next
        return anchor.next





