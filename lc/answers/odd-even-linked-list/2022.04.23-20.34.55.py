class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        even, odd, res_odd = head, head.next, head.next
        while (even.next and even.next.next) or (odd.next and odd.next.next):
            even.next = even.next.next
            if even.next: even = even.next
            odd.next = odd.next.next
            if odd.next: odd = odd.next
        even.next = res_odd
        return head