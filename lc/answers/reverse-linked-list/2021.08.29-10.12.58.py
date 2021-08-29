"""
So a linked list looks like -> 5 -> 3 -> 2 -> 6

We'd iterate through it starting with the head, 5, which points to 3.

We're on 5, seeing that it points to 3. We can start the reversal process there
We can make a new head 3 that points to 5.

Then we have to advance the main pointer from 5 to 3, seeing that it points to 2. On
our second one, we can create a new head 2 and that points to our ret head 3.

As long as there is a next, we can basically transfer it to the other list.

When we're finally at 6, seeing it points to None, we can just return our ret head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head_copy = ListNode(head.val, head.next)
        ret_head = ListNode(head.val, None)
        while head.next:
            ret_head = ListNode(head.next.val, ret_head)
            head = head.next
        return ret_head
