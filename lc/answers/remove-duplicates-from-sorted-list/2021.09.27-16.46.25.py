"""
===== Initial Thoughts =====
simple iterative traversal should work fine here

=== Implemented Approach ===
after taking care of edge cases, maintain a while loop that looks at next. If next
is a node and the same, then tie the next ref to next's next. advance to next's next

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        top = head
        current = head
        while current:
            next_node = current.next
            while next_node and current.val == next_node.val:
                next_node = next_node.next
            current.next = next_node
            current = current.next
        return top