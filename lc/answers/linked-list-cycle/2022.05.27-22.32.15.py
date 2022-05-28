"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if id(head) in seen:
                return True
            seen.add(id(head))
            head = head.next
        return False

but let's solve it in O(1) memory
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next

        while fast and fast.next and fast.next.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False