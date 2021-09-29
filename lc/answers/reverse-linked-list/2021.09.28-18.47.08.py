"""
===== Initial Thoughts =====
let's solve it iteratively again

=== Implemented Approach ===
go through the whole linked list. keep track of the last one you were on. as you go on to the next,
get a ref to the next and point the current to the last. replace last ref with current ref. then move
next to current.


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
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous