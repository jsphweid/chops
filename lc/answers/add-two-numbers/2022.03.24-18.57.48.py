# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
l1 = [2,4,3], l2 = [5,6,4]
remainder=1
[7,0,8]
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        curr = head
        carry = 0
        while l1 or l2 or carry:
            l1_val, l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            carry, nxt_val = divmod(l1_val + l2_val + carry, 10)
            curr.next = ListNode(val=nxt_val, next=None)
            curr = curr.next
        return head.next