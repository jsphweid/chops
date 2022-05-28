class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        