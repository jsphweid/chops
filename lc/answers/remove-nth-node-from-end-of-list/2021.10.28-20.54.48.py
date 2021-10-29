class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        i = 0
        current = head
        lag = None
        while current.next:
            current = current.next
            if lag:
                lag = lag.next
            else:
                if i == n:
                    lag = head
            i += 1
        if not lag:
            if i == n:
                lag = head
                lag.next = lag.next.next
                return head
            else:
                return head.next
        else:
            lag.next.next = lag.next.next.next
            return head