class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        slow, fast, i = head, head.next, 0
        while fast and fast != slow:
            fast = fast.next
            if i & 1:
                slow = slow.next
            i += 1
        return fast == slow