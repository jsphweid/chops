"""
Seems to me that when the arg is None, we should return None

When the first node has no next, then head can simply be returned

The basic strategy once we've figured out if we can early return (see above) is to copy
the head so we have a pointer (current). Then we want a loop that continues executing
until current and current->next == None. In that loop, we want to compare the current val
to next's val. If they are the same, we want to hook the current node to next's next and
increment current to next's next. If that's not the case, then we simply keep traversing
the linked list. Lastly, we want to return the head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle special cases
        if not head:
            return None
        if not head.next:
            return head

        # handle n-length linked list
        current = head
        while current and current.next:
            inner_current = current.next

            while inner_current and inner_current.val == current.val:
                inner_current = inner_current.next

            current.next = inner_current
            current = inner_current

        return head

    # submission failed... maybe because didn't test an even number of nodes?
    # 1->1->2->3, not sure immediately. It seems like that would work...
    # failed on `[1,1,2,3,3]` on `'NoneType' object has no attribute 'next'`

    # so my first mistake was "double jumping" (using `current.next.next` twice)

    # failed a second time because I didn't handle an edge case like [1, 1, 1], damn.
    # it may be back to the drawing board. I incorrectly presumed there would only
    # ever be one duplicate it seems. To correct this, we could create an inner while
    # loop that looks for a different value or None

"""
My issue here was that I failed to see a small logic flaw then failed to consider edge cases.
Once I corrected those, and went through the examples verbally and in my head, my third
submission succeeded.
"""


