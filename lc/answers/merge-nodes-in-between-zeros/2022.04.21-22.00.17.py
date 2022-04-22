"""
I misunderstood the problem, thinking I needed to keep 0's and then altered
my solution slightly.
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        curr = head
        while curr.next:
            nxt = curr.next
            total = 0
            while nxt.val != 0:
                total += nxt.val
                nxt = nxt.next
            head.next = ListNode(total)
            head = head.next
            curr = nxt
        return res.next

But I can do better
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        short = head
        curr = head.next
        total = 0
        while curr:
            total += curr.val
            if curr.val == 0:
                short.next = ListNode(total)
                short = short.next
                total = 0
            curr = curr.next
        return head.next