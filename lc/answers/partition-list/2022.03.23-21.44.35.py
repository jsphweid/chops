"""
===== Initial Thoughts =====
if this weren't a linked list, how would we do this
[1,4,3,2,5,2] x=3
1 2 2 4 3 5

1 2s 4 3 5f 2
once we get to 2, we need to disconnect it, hook up 3 directly
to 5. insert it in between 1 and 4. We can keep another pointer.
It's a singly linked list, so we have to stop one before

slow fast
slow fast both start at first one. What if first is bad?
create a fake head? yes
so slow fast both advance if NEXT number is smaller than x
if next number is x or larger, then advance the fast until its
NEXT is a smaller number. Perform the swap advance both (or let next
round handle it)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        fake = ListNode(val=0, next=head)
        slow = fast = fake
        while fast.next:
            if slow.next.val < x and fast.next.val < x:
                slow = slow.next
                fast = fast.next
            else:
                if fast.next.val < x:
                    node = fast.next
                    fast.next = fast.next.next
                    node.next = slow.next
                    slow.next = node
                    slow = slow.next
                else:
                    fast = fast.next
        return fake.next





