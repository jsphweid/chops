"""
=== Brute Force Approach ===
push everything to a list and get the sequence down using two pointers
then reconstruct

~~Complexity Analysis
Time - O(n)
Space - O(n)

=== Implemented Approach ===
use a stack and the head of the list instead

~~Complexity Analysis
Time - O(n)
Space - O(n)

advance linked list
pop and sever
    reconnect popped to head's next
    point head to popped
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head

        while curr != stack[-1]:
            end = stack.pop()
            end.next = curr.next
            curr.next = end
            if curr == stack[-1]:
                curr = curr.next
                break
            curr = curr.next.next
        curr.next = None
        return head
        