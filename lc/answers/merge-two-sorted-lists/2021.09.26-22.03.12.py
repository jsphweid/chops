"""
===== Initial Thoughts =====
I don't know why this was hard for me last time, but it seems like you should to just be able
to have a while loop and append/advance the smaller of the numbers onto a new list.

=== Implemented Approach ===
while any of the heads are not None, pick the smaller val and increment that list.
With the val, create a new node and put it on the end of the new node.

~~Complexity Analysis
Time - O(m + n)
Space - O(m + n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        output = None
        head = None
        while l1 and l2:
            next_node = None
            if l1.val < l2.val:
                next_node = ListNode(l1.val)
                l1 = l1.next
            else:
                next_node = ListNode(l2.val)
                l2 = l2.next
            if output:
                output.next = next_node
                output = output.next
            else:
                output = head = next_node
        if not output:
            return l1 or l2
        output.next = l1 or l2
        return head