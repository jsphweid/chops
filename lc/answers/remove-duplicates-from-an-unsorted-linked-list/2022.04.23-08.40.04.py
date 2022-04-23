"""
===== Initial Thoughts =====
hard imagining how to solve this one without some state...

=== Brute Force Approach ===
1 pass to find dupes
then alg to skip those

~~Complexity Analysis
Time - O(n)
Space - O(n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counts = Counter()
        curr = head
        while curr:
            counts[curr.val] += 1
            curr = curr.next

        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if counts[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next






