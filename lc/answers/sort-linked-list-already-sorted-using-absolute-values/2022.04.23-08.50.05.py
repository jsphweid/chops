"""
===== Initial Thoughts =====
just separate positives from negatives
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
failed on [0,1,2]

just forgot a return statement
"""
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos, neg = ListNode(0, head), ListNode(0)
        
        # separate positive from negative
        curr_pos, curr_neg = pos, neg
        while curr_pos.next:
            if curr_pos.next.val < 0:
                curr_neg.next = curr_pos.next
                curr_pos.next = curr_pos.next.next
                curr_neg.next.next = None
                curr_neg = curr_neg.next
            else:
                curr_pos = curr_pos.next

        # reverse negative
        prev = None
        curr_neg = neg.next
        while curr_neg:
            nxt = curr_neg.next
            curr_neg.next = prev
            prev = curr_neg
            curr_neg = nxt

        # join
        if neg.next:
            neg.next.next = pos.next
            return prev
        else:
            return pos.next
