# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        res_curr = res
        remainder = 0

        while l1 or l2:
            l1_val = l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            remainder, nxt_val = divmod(l1_val + l2_val + remainder, 10)

            if res == None:
                res = ListNode(nxt_val)
                res_curr = res
            else:
                res_curr.next = ListNode(nxt_val)
                res_curr = res_curr.next
        
        if remainder:
            res_curr.next = ListNode(remainder)

        return res or ListNode(0)