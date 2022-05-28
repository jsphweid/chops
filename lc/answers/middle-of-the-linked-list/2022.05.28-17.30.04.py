"""
=== Brute Force Approach ===
easy way is to count the nodes then do a 2nd pass


~~Complexity Analysis
Time - 2 pass
Space - O(1)

=== Implemented Approach ===
what about slow fast pointer?
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow